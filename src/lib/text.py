import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    This function normalizes input text.

    Input data
    -----------
    text: str,
    *
    casefold: bool = True
    yo2e: bool = True

    Returns
    -------
    Normalized text.
        Type: str

    Tests
    -----
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    """

    if casefold: text = text.casefold()
    if yo2e: text = text.replace("ё", "e").replace("Ё", "Е")
    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    while "  " in text: text = text.replace("  ", " ")
    return text.strip()


def tokenize(text: str) -> list [str]:
    """
    This function tokenizes input (normalized) text.

    Input data
    -----------
    text: str

    Returns
    -------
    List of tokens.
        Type: list [str]

    Tests
    -----
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    """
    tokens = re.findall(r"\w+(?:-\w+)*", text)
    return tokens

def count_freq(tokens: list[str]) -> dict [str, int]:
    """
    It counts frequencies for tokens.

    Input data
    -----------
    tokens: list[str]

    Returns
    -------
    List of frequencies for tokens.
        Type: dict [str, int]

    Tests
    -----
    freq = count_freq(["a","b","a","c","b","a"])
    assert freq == {"a":3, "b":2, "c":1}
    """
    freqs = {}
    for t in sorted(tokens):
        c = tokens.count(t)
        freqs.update({t: c})
    return freqs

def top_n(freq: dict[str, int], n: int = 5) -> list [ tuple [str, int] ]:
    """
    It returns TOP-n of tokens by frequencies.

    Input data
    -----------
    freq: dict[str, int]
    n: int = 5

    Returns
    -------
    TOP-n.
        Type: list [ tuple [str, int] ]

    Tests
    -----
    1.
        freq = count_freq(["a","b","a","c","b","a"])
        assert freq == {"a":3, "b":2, "c":1}
        assert top_n(freq, 2) == [("a",3), ("b",2)]
    2.
        freq2 = count_freq(["bb","aa","bb","aa","cc"])
        assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
    """
    items = [i for i in freq.items()]
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:n]
