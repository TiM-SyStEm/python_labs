from collections import Counter
import os
from sys import path, stdin
from io_txt_csv import read_text, write_csv

path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.lib.text import normalize, tokenize

def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
