import argparse
from collections import Counter
from pathlib import Path

from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import count_freq, normalize, tokenize


def frequencies_from_text(text: str) -> list [str]:
    """
    Returns tokens from input text

    Input data
    ----------
    text: str
        Input text.

    Returns
    -------
    Return list of tokens.
    """
    tokens = tokenize(normalize(text))
    return tokens

def ru_key(s: str) -> tuple:
    """
    Returns key for correct sorting with russian characters.

    Input data
    ----------
    s: str
        Input text.

    Returns
    -------
    Return tuple.
    """
    _RU_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    _RU_ORDER = {ch: i for i, ch in enumerate(_RU_ALPHABET)}
    result = []
    for ch in s:
        if ch in _RU_ORDER:
            result.append((0, -_RU_ORDER[ch]))
        else:
            result.append((1, -ord(ch)))
    return tuple(result)

def build_per_file_rows(paths: list[str], encoding: str = "utf-8") -> list[tuple[str, str, int]]:
    """
    It returns strings for report for every file.
    Sorted: file ↑, count ↓, word ↑.

    Input data
    -----------
    paths: list[Path]
    encoding: str = "utf-8"

    Returns
    -------
    list[tuple[str, str, int]]
    """
    rows: list[tuple[str, str, int]] = []

    for p in paths:
        text = read_text(p, encoding=encoding)
        counter = count_freq(frequencies_from_text(text))

        for word, count in counter.items():
            rows.append((Path(p).name, word, count))

        print(f"{Path(p).name}: \"{text.strip()}\"")

    rows.sort(key=lambda r: (r[0], -r[2], ru_key(r[1])))
    return rows


def build_total_rows(paths: list[str], encoding: str = "utf-8") -> list[tuple[str, int]]:
    """
    It returns list for total report.
    Sorted: count ↓, word ↑.

    Input data
    ----------
    paths: list[Path],
    encoding: str = "utf-8"

    Returns
    -------
    list[tuple[str, int]]
    """
    total: Counter = Counter()

    for p in paths:
        text = read_text(p, encoding=encoding)
        total.update(frequencies_from_text(text))

    rows = [(word, count) for word, count in total.items()]
    rows.sort(key=lambda r: (-r[1], ru_key(r[0])))
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--in",
        dest="inputs",
        nargs="+",
        required=True
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        required=False
    )
    args = parser.parse_args()

    per_file_rows = build_per_file_rows(args.inputs, args.encoding)
    per_file_path = "../../data/lab04/report_per_file.csv"

    write_csv(per_file_rows, per_file_path, header=("file", "word", "count"))

    total_rows = build_total_rows(args.inputs, args.encoding)
    total_path = "../../data/lab04/report_total.csv"

    write_csv(total_rows, total_path, header=("word", "count"))

    print()

    with open(per_file_path, "r", encoding="utf-8") as f:
        print("report_per_file.csv")
        print(f.read().strip())

    print()

    with open(total_path, "r", encoding="utf-8") as f:
        print("report_total.csv")
        print(f.read().strip())

if __name__ == "__main__":
    main()
