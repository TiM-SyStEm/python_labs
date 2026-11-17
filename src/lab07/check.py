import random

from src.lab07.search import binary_search, linear_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials=100) -> int:
    """
    Check sorting function with random data.

    Input data
    ----------
    fn:
        Callable object of function.
    trials = 100:
        Trials of checking.

    Returns
    -------
    Returns count of sucsesfully checks.
    """
    checks = 0
    for _ in range(trials):
        length = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(length)]
        original = nums.copy()

        res = fn(nums)
        assert res == sorted(original), f"Error in sorting {fn.__name__}: {res} != {sorted(original)}"
        assert nums == original, f"has been {fn.__name__}"
        checks += 1

    return checks


def check_search(trials=100) -> int:
    """
    Checks linear and binary search include extremes and absents values.

    Input data
    ----------
    trials = 100:
        Trials of checking.

    Returns
    -------
    Returns count of sucsesfully checks.
    """
    checks = 0

    for _ in range(trials):
        length = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(length)]

        # Peek candidates from nums for searching include extremes and absents
        candidates = [-110, 110]
        if nums:
            candidates.extend([nums[0], nums[-1], random.choice(nums)])

        for x in candidates:
            res_lin = linear_search(nums, x)
            try:
                expected_idx = nums.index(x)
            except ValueError:
                expected_idx = -1

            assert res_lin == expected_idx, f"linear_search({nums}, {x}) -> {res_lin}, expected {expected_idx}"
            checks += 1

        sorted_nums = sorted(nums)
        for x in candidates:
            res_bin = binary_search(sorted_nums, x)
            if x in sorted_nums:
                assert 0 <= res_bin < len(sorted_nums) and sorted_nums[res_bin] == x, (
                    f"binary_search({sorted_nums}, {x}) returned wrong index {res_bin}"
                )
            else:
                assert res_bin == -1, f"binary_search({sorted_nums}, {x}) -> {res_bin}, expected -1"
            checks += 1

    return checks


def check_two_sum(trials=100) -> int:
    """
    Check 2 algorithms for two_sums.

    Input data
    ----------
    trials = 100:
        Trials of checking.

    Returns
    -------
    Returns count of sucsesfully checks.
    """
    checks = 0

    for _ in range(trials):
        length = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(length)]

        targets = [random.randint(-110, 110)]
        if length >= 2:
            i, j = random.sample(range(length), 2)
            targets.append(nums[i] + nums[j])

        for target in targets:
            res_brute = two_sum_brute(nums, target)
            res_fast = two_sum_fast(nums, target)

            if res_brute is None:
                assert res_fast is None, f"When target={target}: brute=None, fast={res_fast}"
            else:
                assert res_fast is not None, f"When target={target}: brute={res_brute}, fast=None"

                val1, val2 = res_brute
                assert val1 + val2 == target, f"two_sum_brute returned wrong pair {res_brute} for target={target}"

                idx1, idx2 = res_fast
                assert idx1 != idx2 and nums[idx1] + nums[idx2] == target, (
                    f"two_sum_fast returned wrong pair {res_fast} for target={target}"
                )
            checks += 1

    return checks


def main():
    # Set up random seed
    random.seed(42)

    total_checks = 0

    print("[PROCESSING] Sorting and searching modules check has been started")

    for sort_fn in (bubble_sort, insertion_sort, selection_sort):
        total_checks += check_sorting(sort_fn, trials=100)
    total_checks += check_search(trials=100)

    total_checks += check_two_sum(trials=100)

    print(f"{"[OK]" if total_checks == 1481 else "WARNING"} Modules passed all 1481 checks")

if __name__ == "__main__":
    main()
