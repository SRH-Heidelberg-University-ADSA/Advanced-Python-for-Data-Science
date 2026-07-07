def read_file(path):
    """
    Reads the content of a file at the given path and returns it as a string.
    """
    with open(path, "r") as f:
        return f.read()