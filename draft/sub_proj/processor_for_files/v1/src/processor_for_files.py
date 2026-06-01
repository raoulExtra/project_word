# See: requi/visit/README.md for usage documentation
import os
import sys
import pathlib
import argparse
import yaml


def process_files(kind: str, action: str, root: pathlib.Path, ext: str = None) -> int:
    valid_kinds = {"frontmatter"}
    valid_actions = {"visit"}
    if kind not in valid_kinds:
        raise ValueError(f"Unknown kind: {kind}")
    if action not in valid_actions:
        raise ValueError(f"Unknown action: {action}")
    if action == "visit":
        return _visit_files(kind, root, ext)


def _visit_files(kind: str, root: pathlib.Path, ext: str = None) -> int:
    roots = _parse_roots(root)
    log_entries = []
    for r in roots:
        for filepath in _scan_files(r, ext):
            if kind == "frontmatter":
                is_valid, missing_fields = _validate_frontmatter(filepath)
                if missing_fields:
                    log_entries.append(f"{filepath}: missing {', '.join(missing_fields)}")
            print(filepath)
    if log_entries:
        _write_log(log_entries)
    return 0


def _validate_frontmatter(filepath: str) -> tuple:
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except (IOError, OSError):
        return False, ['id', 'kind']
    if '```yaml' not in content:
        return False, ['yaml delimiter']
    start = content.find('```yaml') + len('```yaml')
    end = content.find('```', start)
    if end == -1:
        return False, ['yaml closing delimiter']
    yaml_content = content[start:end].strip()
    try:
        data = yaml.safe_load(yaml_content)
    except yaml.YAMLError:
        return False, ['id', 'kind']
    if not data:
        return False, ['id', 'kind']
    missing = []
    if 'id' not in data:
        missing.append('id')
    if 'kind' not in data:
        missing.append('kind')
    return len(missing) == 0, missing


def _write_log(entries: list) -> None:
    log_path = pathlib.Path('/home/peter/sync/project_word/draft/sub_proj/processor_for_files/data/visit_log.txt')
    log_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(log_path, 'w') as f:
            for entry in entries:
                f.write(entry + '\n')
    except (IOError, OSError) as e:
        raise RuntimeError(f"Cannot write log file: {e}") from e


def _parse_roots(root) -> list:
    if isinstance(root, str):
        return [pathlib.Path(r.strip()) for r in root.split(',')]
    return [pathlib.Path(root)]


def _scan_files(root: pathlib.Path, ext: str = None):
    for dirpath, dirnames, filenames in os.walk(root, followlinks=True):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for filename in filenames:
            if filename.startswith('.'):
                continue
            if ext and not filename.endswith(f'.{ext}'):
                continue
            yield os.path.join(dirpath, filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--kind', required=True)
    parser.add_argument('--action', required=True)
    parser.add_argument('--root', required=True)
    parser.add_argument('--ext', default=None)
    
    args = parser.parse_args()
    sys.exit(process_files(args.kind, args.action, pathlib.Path(args.root), args.ext))