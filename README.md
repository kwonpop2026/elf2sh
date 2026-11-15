# elf2sh

Convert ELF executable binaries into self-extracting Bash scripts.

`elf2sh` packages an executable inside a shell script. When the generated script runs, it restores the embedded binary to a temporary file, passes through command-line arguments, executes it, and removes the temporary file when it exits.

## Features

- Convert an executable binary into a standalone `.sh` file
- Restore the binary automatically at runtime
- Forward command-line arguments to the original executable
- Remove the temporary binary after execution
- No third-party Python dependencies

## Requirements

- Python 3.8 or newer
- Bash
- The `base64` command

## Usage

```bash
python3 elf2sh.py INPUT_BINARY OUTPUT_SCRIPT
chmod +x OUTPUT_SCRIPT
./OUTPUT_SCRIPT [ARGUMENTS...]
```

Example:

```bash
python3 elf2sh.py ./hello ./hello.sh
chmod +x ./hello.sh
./hello.sh world
```

The generated script can be copied to another compatible Linux system that has Bash and `base64` available. The embedded executable must be compatible with the target system.

## How it works

1. `elf2sh` reads the input binary.
2. The binary is Base64-encoded and inserted into a Bash script.
3. The generated script decodes the binary into a temporary file when run.
4. The temporary file is made executable and launched with the supplied arguments.
5. A shell `trap` removes the temporary file when the script exits.

## Security notice

Only convert and execute binaries from sources you trust. `elf2sh` packages binaries; it does not inspect, sandbox, or verify their contents. Running an untrusted generated script can be dangerous.

## License

This project is licensed under the [MIT License](LICENSE).
