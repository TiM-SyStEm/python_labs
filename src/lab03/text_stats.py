import os
from sys import path, stdin

path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from src.lib.text import *

TABLE_MODE = True

text = stdin.read()
text_nrm = normalize(text)
tokens = tokenize(text_nrm)
freqs = count_freq(tokens)
top_5 = top_n(freqs, 5)

print(f"Всего слов: {len(tokens)}\nУникальных слов: {len(freqs.keys())}\nТоп-5:")

if TABLE_MODE:
    max_len = max(len(k) for k in freqs)

    print(f"{"слово":<{max_len}}| частота")
    print("-"*( max_len + 9 ))

    for item in top_5:
        w, f = item
        print(f"{w:<{max_len}}| {f}")
else:
    for item in top_5:
        w, f = item
        print(f"{w}:{f}")
