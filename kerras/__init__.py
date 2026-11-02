from pathlib import Path

def get_code_files():
    """Return the available TXT and PDF files."""
    folder = Path(__file__).parent / "codes"
    return sorted(
        file for file in folder.iterdir()
        if file.suffix.lower() in {".txt", ".pdf"}
    )
