#!/usr/bin/env python3
"""Mirror the published Handgrown skills into this repository.

The skills are written once, in the Handgrown product repository, and published on
https://app.handgrown.app/integrations (deployed with every release) with a manifest of sha256 digests. This script downloads
the published bundles, checks them against the manifest, and writes the files this repository
mirrors. `.handgrown-sync.json` records every mirrored file and its digest.

  python3 scripts/sync_from_handgrown.py            # download and write
  python3 scripts/sync_from_handgrown.py --local D  # use bundles already in directory D
  python3 scripts/sync_from_handgrown.py --check    # fail if a mirrored file was edited by hand
"""
import argparse
import hashlib
import io
import json
import sys
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / '.handgrown-sync.json'
SOURCE = 'https://app.handgrown.app/integrations'
BUNDLES = ('handgrown-agent-kit.zip', 'handgrown-brand-operations.zip')


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(base: str, local: Path | None, name: str) -> bytes:
    if local:
        return (local / name).read_bytes()
    request = urllib.request.Request(f'{base}/{name}', headers={'user-agent': 'handgrown-agent-skills-sync'})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def safe(path: str) -> PurePosixPath:
    pure = PurePosixPath(path)
    if pure.is_absolute() or '..' in pure.parts or not pure.parts:
        raise SystemExit(f'Refusing unsafe path in bundle: {path}')
    return pure


def mirrored_files(base: str, local: Path | None) -> tuple[str, dict[str, bytes]]:
    manifest = json.loads(fetch(base, local, 'manifest.json'))
    expected = {f['name']: f for f in manifest['files']}
    files: dict[str, bytes] = {}
    for name in BUNDLES:
        data = fetch(base, local, name)
        entry = expected.get(name)
        if not entry or entry['sha256'] != digest(data) or entry['bytes'] != len(data):
            raise SystemExit(f'{name} does not match the published manifest; not syncing')
        with zipfile.ZipFile(io.BytesIO(data)) as bundle:
            for info in bundle.infolist():
                if info.is_dir():
                    continue
                path = safe(info.filename)
                if name == 'handgrown-agent-kit.zip' and path.parts[0] == 'skills':
                    files[str(path)] = bundle.read(info)
                elif name == 'handgrown-brand-operations.zip' and path.parts[0] == 'handgrown-brand-operations':
                    files[str(PurePosixPath('skills') / path)] = bundle.read(info)
                    if path == PurePosixPath('handgrown-brand-operations/references/PROJECT_INSTRUCTIONS.md'):
                        files['PROJECT_INSTRUCTIONS.md'] = bundle.read(info)
    if not files:
        raise SystemExit('The published bundles held no skills; not syncing')
    return manifest['version'], files


def check() -> int:
    record = json.loads(RECORD.read_text())
    edited = [p for p, sha in record['files'].items() if not (ROOT / p).is_file() or digest((ROOT / p).read_bytes()) != sha]
    if edited:
        print('These files are mirrored from Handgrown and were changed by hand:', *edited, sep='\n  ')
        print('Change them in the Handgrown repository (integrations/handgrown-claude) instead.')
        return 1
    print(f'{len(record["files"])} mirrored files match the last sync.')
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--local', type=Path)
    parser.add_argument('--source', default=SOURCE)
    args = parser.parse_args()
    if args.check:
        return check()
    version, files = mirrored_files(args.source.rstrip('/'), args.local)
    previous = json.loads(RECORD.read_text())['files'] if RECORD.exists() else {}
    for stale in sorted(set(previous) - set(files)):
        (ROOT / stale).unlink(missing_ok=True)
    for path, data in files.items():
        target = ROOT / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    RECORD.write_text(json.dumps({'source': args.source if not args.local else SOURCE, 'manifest_version': version,
                                  'files': {p: digest(d) for p, d in sorted(files.items())}}, indent=2) + '\n')
    print(f'Mirrored {len(files)} files from manifest {version}.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
