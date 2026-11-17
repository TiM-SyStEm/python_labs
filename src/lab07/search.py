from tabnanny import check


def linear_search(nums, x) -> int:
    """
    Linear search x in nums and returns index of element. Returns -1 if it wasn't find.

    Input data
    ----------
    nums:
        Array of nums.
    x:
        Searching element.

    Returns
    -------
    First founded index of element or -1.
    """
    for i in range(len(nums)):
        if nums[i] == x:
            return i

    return -1


def binary_search(sorted_nums, x) -> int:
    """
    Binary search in ascending order sorted array. / O(log(n))

    Input data
    ----------
    sorted_nums:
        Ascending order sorted array.
    x:
        Searching element.

    Returns
    -------
    First founded index of element or -1.
    """
    l = 0
    r = len(sorted_nums) - 1

    while l <= r:
        mid = (l+r)//2

        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1

def two_sum_brute(nums, target) -> tuple[int, int] | None:
    """
    Find pair with sum of elements equals targt value and returns it. It returns None, if array hasn't such pair. / O(n^2)

    Input data
    ----------
    nums:
        Array of numbers.
    target:
        Target sum of pair.

    Returns
    -------
    Pair of elements.
        tuple[int, int] | None
    """
    n = len(nums)

    for i in range(n):
        for j in range(n):
            if i != j:
                x = nums[i]
                y = nums[j]
                if x + y == target:
                    return x, y

def two_sum_fast(nums, target) -> tuple[int, int] | None:
    """
    Fast algorithm for finding pair with sum of elements equals targt value. It returns None, if array hasn't such pair. / O(n)

    Input data
    ----------
    nums:
        Array of numbers.
    target:
        Target sum of pair.

    Returns
    -------
    Pair of elements.
        tuple[int, int] | None
    """
    checked = {}

    for i, num in enumerate(nums):
        need = target - num

        if need in checked:
            return checked[need], i

        checked[num] = i

    return None
