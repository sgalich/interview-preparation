from typing import Union, List


def sort(arr: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    """Merge Sort algorithm.
    O(n*log(n))
    """

    def merge(left, right):
        new_array = []
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                new_array.append(left[l])
                l += 1
            else:
                new_array.append(right[r])
                r += 1
        if l == len(left):
            new_array += right[r:]
        else:
            new_array += left[l:]
        return new_array

    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]    # 1. Divide into 2 parts
    left, right = sort(left), sort(right)    # 2. Sort each part recursively
    # 3. Merge 2 parts
    return merge(left, right)
