# Лабораторная работа 7
## Сортировки
```py
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
```

## Поиск
```py
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
```

## Бенчмарки
| ![Скриншот №1](../../images/lab07/img01.png "Вывод в консоль результат бенчмарков") |
| :--: |
| Рис 1. Вывод в консоль результат бенчмарка |

| ![Скриншот №2](../../images/lab07/img01.png "Таблица результатов бенчмарка") |
| :--: |
| Рис 2. Таблица результатов бенчмарка |
