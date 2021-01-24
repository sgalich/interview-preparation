from typing import Union, List


def sort(arr: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    """Insertion sort algorithm.
    O(n^2)
    """
    arr = arr.copy()
    if len(arr) < 2:
        return arr
    for i in range(1, len(arr)):
        num = arr[i]
        # Linear backwards search
        for j in range(i-1, -1, -1):
            if num < arr[j]:
                arr[j], arr[j + 1] = num, arr[j]
            else:
                break
    return arr
