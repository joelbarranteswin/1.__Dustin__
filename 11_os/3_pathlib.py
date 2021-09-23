from pathlib import Path

entries = Path('11_os/')
for entry in entries.iterdir():
    print(entry.name)