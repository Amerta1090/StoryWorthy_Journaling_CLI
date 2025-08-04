#!/bin/bash

# Path ke virtual environment dan script Python
VENV_PATH="/home/amerta/Documents/Journal CLI/venv"
SCRIPT_PATH="/home/amerta/Documents/Journal CLI/journal.py"

# Aktifkan virtual environment
source "$VENV_PATH/bin/activate"

# Jalankan script Python dengan argumen yang diteruskan
python "$SCRIPT_PATH" "$@"

# Menonaktifkan virtual environment secara otomatis setelah script selesai
deactivate
