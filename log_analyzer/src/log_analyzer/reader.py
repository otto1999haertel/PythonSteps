# src/log_analyzer/reader.py
from pathlib import Path
from typing import Iterator

def read_lines(path: Path) -> Iterator[str]:
    """Liefert alle Zeilen einer Datei als Generator."""
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")