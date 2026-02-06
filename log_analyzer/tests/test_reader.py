from pathlib import Path
from log_analyzer import read_lines

def test_read_lines(tmp_path: Path):
    f = tmp_path / "sample.log"
    f.write_text("line1\nline2\nline3")
    
    lines = list(read_lines(f))
    assert lines == ["line1", "line2", "line3"]