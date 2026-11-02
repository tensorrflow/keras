from pathlib import Path

def get_code_files():
    """Return the available Deep Learning code files."""
    folder = Path(__file__).parent / "codes"
    return list(folder.glob("*.txt"))
