from log_analyzer.stats import count_by_level


def test_count_by_level():
    entries = [
        {"level": "INFO"},
        {"level": "ERROR"},
        {"level": "INFO"},
        {"level": "WARN"},
        {"level": "ERROR"},
    ]

    counts = count_by_level(entries)

    assert counts["INFO"] == 2
    assert counts["ERROR"] == 2
    assert counts["WARN"] == 1