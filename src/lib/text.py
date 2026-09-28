import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold: text = text.casefold()
    if yo2e: text = text.replace("ё", "e").replace("Ё", "Е")
    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    while "  " in text: text = text.replace("  ", " ")
    return text.strip()


def tokenize(text: str) -> list [str]:
    tokens = re.findall(r"\w+(?:-\w+)*", text)
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:
    freqs = {}
    for t in sorted(tokens):
        c = tokens.count(t)
        freqs.update({t: c})
    return freqs

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = [i for i in freq.items()]
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:n]
