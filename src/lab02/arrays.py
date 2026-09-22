def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    This function takes list and return pair (min, max) of the list.

    Input data
    -----------
    nums: list [float or int]

    Returns
    -------
    Pair (min, max)
        Type: tuple [float | int, float | int]

    Raises
    ------
    ValueError: List is empty.
    """

    if len(nums) == 0:
        raise ValueError("List is empty.")
    return min(nums), max(nums)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    It takes list and return ascending sorted list with only unique values.

    Input data
    ----------
    nums: list [float | int]

    Returns
    -------
    Ascending sorted list with only unique values.
        Type: list [float | int]
    """

    return list(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    """
    It takes list with lists or tuples and flatten its at common list.

    Input data
    ----------
    mat: list [list | tuple]

    Returns
    -------
    Flatten list.
        Type: list

    Raises
    ------
    TypeError: Unexpected 1 or more elements that aren't list or tuple.
    """

    buf = []
    for m in mat:
        if type(m) == list or type(m) == tuple:
            buf += [*tuple(m)]
        else:
            raise TypeError("There are 1 or more elements that aren't list or tuple.")
    return buf
