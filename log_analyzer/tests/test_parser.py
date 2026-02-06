from log_analyzer import parse_line
from log_analyzer.reader import read_lines


def test_parse_log_line():
    line = "2024-01-10 ERROR Database connection failed"

    entry = parse_line(line)

    assert entry["date"] == "2024-01-10"
    assert entry["level"] == "ERROR"
    assert entry["message"] == "Database connection failed"