#!/bin/bash
# Script wrapper untuk menjalankan daemon
# Path akan disesuaikan dengan lokasi clone repository

# Dapatkan direktori script ini
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Direktori project (parent dari folder service)
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Jalankan daemon dengan path yang dinamis
/usr/bin/python3 "$PROJECT_DIR/src/mydaemon.py"
