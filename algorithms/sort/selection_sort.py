from typing import Union, List


def sort(arr: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    """Selection sort algorithm.
    O( ? )
    """
    arr = arr.copy()
    for i in range(len(arr)):
        num = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < num:
                arr[i] = arr[j]
                arr[j] = num
                num = arr[i]
    return arr
