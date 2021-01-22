from typing import Union, List


def sort(arr: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    """Binary Insertion sort algorithm.
    O(n^2)
    """

    def binary_search(num: Union[int, float, str], end: int, start=0) -> int:
        while end > start:
            ind = start + int((end - start) / 2)
            if arr[ind] < num:
                start = ind + 1
            elif ind > 0 and arr[ind - 1] > num:
                end = ind
            else:
                return ind

    if len(arr) < 2:
        return arr
    for i in range(1, len(arr)):
        num = arr[i]
        j = binary_search(num, i + 1)
        arr = arr[:j] + [num] + arr[j:i] + arr[i + 1:]
    return arr
