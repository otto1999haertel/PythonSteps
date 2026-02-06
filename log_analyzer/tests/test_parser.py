from log_analyzer import parse_line

def test_parse_line():
    line = "2024-01-10 ERROR Database failure"
    entry = parse_line(line)
    
    assert entry["date"] == "2024-01-10"
    assert entry["level"] == "ERROR"
    assert entry["message"] == "Database failure"