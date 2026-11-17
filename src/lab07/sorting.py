def bubble_sort(nums):
    """
    Bubble sorting function. / O(n^2)

    Input data
    ----------
    nums
        Array of numbers.

    Returns
    -------
    New ascending order sorted array.
    """
    arr = nums.copy()
    n = len(arr)
    change = False

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                change = True
        if not change:
            # Exit early if array is already sorted
            break
    return arr

def insertion_sort(nums):
    """
    Insertion sorting function. / O(n^2)

    Input data
    ----------
    nums
        Array of numbers.

    Returns
    -------
    New ascending order sorted array.
    """
    arr = nums.copy()

    for i in range(1, len(arr)):
        num = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > num:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = num

    return arr


def selection_sort(nums):
    """
    Selection sorting function. / O(n^2)

    Input data
    ----------
    nums
        Array of numbers.

    Returns
    -------
    New ascending order sorted array.
    """
    arr = nums.copy()

    for i in range(len(arr)):
        min_pos = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_pos]: min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]

    return arr
