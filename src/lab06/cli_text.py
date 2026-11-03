import argparse

from src.lab04.io_txt_csv import read_text
from src.lab04.text_report import sorted_word_counts
from src.lib.text import *


def main():
    parser = argparse.ArgumentParser(description="CLI‑utils for lab №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Print lines from file.")
    cat_parser.add_argument(
        "--input",
        dest="input_file",
        required=True
    )
    cat_parser.add_argument("-n", action="store_true", help="Numurate strings.")

    stats_parser = subparsers.add_parser("stats", help="Freqs of words")
    stats_parser.add_argument(
        "--input",
        dest="input_file",
        required=True,
        help="Input path."
    )
    stats_parser.add_argument(
        "--top",
        dest="top_n",
        required=False,
        type=int,
        default=5,
        help="Count of top tokens. Default: 5."
    )

    args = parser.parse_args()

    if args.command == "cat":
        with open(args.input_file, "r", encoding="utf-8") as f:
            for c, l in enumerate(f.readlines()):
                if args.n:
                    print(f"[{c}]", l, end="")
                else:
                    print(l, end="")

    elif args.command == "stats":
        text = read_text(args.input_file, encoding="utf-8")
        nrm_text = normalize(text)
        tokens = tokenize(nrm_text)
        freqs = dict(sorted_word_counts(count_freq(tokens)))

        if text != "":
            top_5 = top_n(freqs, args.top_n)

            print(f"Всего слов: {len(tokens)}\nУникальных слов: {len(freqs.keys())}\nТоп-5:")

            max_len = max(len(k) for k in freqs)

            print(f"{"слово":<{max_len}}| частота")
            print("-"*( max_len + 9 ))

            for item in top_5:
                w, f = item
                print(f"{w:<{max_len}}| {f}")

if __name__ == "__main__":
    main()
