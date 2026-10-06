import csv
from collections.abc import Iterable, Sequence
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    It reads text from file with choosed encoding.

    Input data
    -----------
    path: str | Path
        Path to file.
    encoding = "utf-8": str
        Choosed encoding. You can choose another encoding, for example: encoding="cp1251".

    Returns
    -------
    Text from file.
        Type: str

    Exceptions
    ----------
    FileNotFoundError
    UnicodeDecodeError
    """
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
    header: tuple[str, ...] | None = None) -> None:
    """
    It writes CSV-table with header and rows by path.

    Input data
    -----------
    rows: Iterable[Sequence]
    path: str | Path
        Path to file.
    header: tuple[str, ...] | None = None

    Returns
    -------
    None

    Exceptions
    ----------
    ValueError: rows must has similar length.
    """
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)

        for r in range(len(rows)):
            if len(rows[r]) == len(rows[0]):
                w.writerow(rows[r])
            else:
                raise ValueError("rows must has similar length.")

def ensure_parent_dir(path: str | Path) -> None:
    """
    Creates parent directory for file if it wasn't.

    Input data
    -----------
    path: str | Path
        Full path to file!

    Returns
    -------
    None
    """
    path = Path(path)
    parts = path.parts
    if not Path(*parts[:-1]).exists():
        Path(*parts[:-1]).mkdir()
        return
