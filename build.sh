#!/bin/bash -e

python -OO -m PyInstaller \
  --noconfirm \
  --console \
  --onefile \
rst2.py