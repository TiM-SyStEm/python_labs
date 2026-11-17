import csv
import random
import timeit
from pathlib import Path

from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import *
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def generation_data(n):
    path = Path(__file__).parents[2] / "data" / "lab07" / "samples" / f"numbers_{n}.csv"

    if path.exists():
        return

    rows = [[random.randint(0, 1_000_000)] for _ in range(n)]
    write_csv(rows, path, ("value",))


def read_numbers(path):
    with open(path, encoding="utf-8") as f:
        return [int(row["value"]) for row in csv.DictReader(f)]


def bench_sorts(n):
    data = read_numbers(f"data/lab07/samples/numbers_{n}.csv")
    rows = []
    t = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", t))

    funcs = (
        ("bubble_sort", bubble_sort),
        ("insertion_sort", insertion_sort),
        ("selection_sort", selection_sort),
    )

    for name, fun in funcs:
        if n >= 100000:
            rows.append(("sort", n, name, ">60"))
            continue

        arr = data.copy()
        start = timeit.default_timer()
        fun(arr)
        t = timeit.default_timer() - start

        rows.append(("sort", n, name, ">60" if t > 60 else t))

    return rows


def bench_search(n):
    data = read_numbers(f"data/lab07/samples/numbers_{n}.csv")
    sorted_data = sorted(data)
    target = -1  # Ищем отсутствующий элемент (худший случай для линейного поиска)
    rows = []

    # Замер встроенного оператора `in` как базового ориентира
    t = timeit.timeit(lambda: target in data, number=1)
    rows.append(("search", n, "in", t))

    funcs = (
        ("linear_search", linear_search, data),
        ("binary_search", binary_search, sorted_data),
    )

    for name, fun, arr in funcs:
        start = timeit.default_timer()
        fun(arr, target)
        t = timeit.default_timer() - start

        rows.append(("search", n, name, ">60" if t > 60 else t))

    return rows


def bench_two_sum(n):
    data = read_numbers(f"data/lab07/samples/numbers_{n}.csv")
    target = -1
    rows = []

    funcs = (
        ("two_sum_brute", two_sum_brute),
        ("two_sum_fast", two_sum_fast),
    )

    for name, fun in funcs:
        if n >= 100000 and name == "two_sum_brute":
            rows.append(("two_sum", n, name, ">60"))
            continue

        start = timeit.default_timer()
        fun(data, target)
        t = timeit.default_timer() - start

        rows.append(("two_sum", n, name, ">60" if t > 60 else t))

    return rows

def print_table(rows, headers=("task", "n", "func", "secs")):
    header_line = f"{headers[0]:<10} | {headers[1]:>8} | {headers[2]:<16} | {headers[3]:>10}"
    print(header_line)
    print("-" * len(header_line))

    for task, n, func, secs in rows:
        secs_str = f"{secs:.6f}" if isinstance(secs, float) else f"{secs:>10}"
        print(f"{task:<10} | {n:>8} | {func:<16} | {secs_str:>10}")


def main():
    random.seed(42)

    ns = [1_000, 10_000, 100_000]
    rows = []

    for n in ns:
        generation_data(n)
        rows.extend(bench_sorts(n))
        rows.extend(bench_search(n))
        rows.extend(bench_two_sum(n))

    out_path = Path(__file__).parents[2] / "data" / "lab07" / "out" / "bench.csv"
    write_csv(rows, out_path, ("task", "n", "func", "secs"))
    print_table(rows)


if __name__ == "__main__":
    main()
