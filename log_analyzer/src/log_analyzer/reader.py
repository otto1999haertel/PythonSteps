def read_lines(file_path):
    print(f"Reading lines from file: {file_path}")
    with open(file_path, "r") as f:
        for line in f:
            yield line.strip()