#!/usr/bin/env python3
import argparse
import base64
from pathlib import Path
TEMPLATE = """#!/bin/bash
set -e

BIN="$(mktemp)"
trap 'rm -f "$BIN"' EXIT

base64 -d > "$BIN" <<'DATA'
{data}
DATA

chmod +x "$BIN"
exec "$BIN" "$@"
"""

def main():
    parser = argparse.ArgumentParser(
        prog="elf2sh",
        description="Convert executable files to self-extracting shell scripts."
    )
    parser.add_argument("input", help="Input executable file")
    parser.add_argument("output", help="Output shell script")
    args = parser.parse_args()
    data = Path(args.input).read_bytes()
    encoded = base64.b64encode(data).decode('ascii')
    script = TEMPLATE.format(data=encoded)
    Path(args.output).write_text(script)
    print(f"[+] Created: {args.output}")

if __name__ == '__main__':
    main()
