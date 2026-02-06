from pathlib import Path
from log_analyzer.reader import read_lines  # Korrekt

def test_read_lines(tmp_path: Path):
    log_file = tmp_path / "sample.log"
    
    lines = list(read_lines(log_file))