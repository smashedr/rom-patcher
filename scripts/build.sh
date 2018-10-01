#!/usr/bin/env bash

set -e

[[ -n "$1" ]] && spec_name="$1" || spec_name="main.spec"

[[ ! -f "${spec_name}" ]] && echo "Unable to stat spec file: ${spec_name}" && exit 1

[[ ! -d "bin" ]] && echo "Missing the required bin directory." && exit 1

[[ -d "build" ]] && rm -rf "build"
[[ -d "dist" ]] && rm -rf "dist"
[[ -d "__pycache__" ]] && rm -rf "__pycache__"

python3 -m PyInstaller --clean "$spec_name"
