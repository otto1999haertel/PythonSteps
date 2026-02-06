# src/log_analyzer/parser.py
from typing import Dict

def parse_line(line: str) -> Dict[str, str]:
    """
    Erwartet Format:
    YYYY-MM-DD LEVEL Message
    Beispiel:
    2024-01-10 ERROR Database connection failed
    """
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError(f"Ungültige Logzeile: {line}")
    date, level, message = parts
    return {"date": date, "level": level, "message": message}