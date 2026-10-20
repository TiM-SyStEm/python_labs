import argparse
from collections import Counter

from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import count_freq, normalize, tokenize, top_n


def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

def args_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument(
         "--in", "-i",
        dest="input_file",
        required=True
    )
    parser.add_argument(
         "--out", "-o",
        dest="out_file",
        required=True
    )
    parser.add_argument(
         "--encoding", "-e",
        dest="encoding",
        default="utf-8",
        required=False
    )
    return parser.parse_args()

def main():
    args = args_parse()
    text = read_text(args.input_file, encoding=args.encoding)
    nrm_text = normalize(text)
    tokens = tokenize(nrm_text)
    freqs = dict(sorted_word_counts(count_freq(tokens)))

    write_csv(freqs.items(), args.out_file, header=("word", "count"))

    if text != "":
        TABLE_MODE = False

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

if __name__ == "__main__":
    main()
