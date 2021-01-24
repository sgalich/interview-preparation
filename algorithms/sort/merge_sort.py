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

    arr = arr.copy()
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]    # 1. Divide into 2 parts
    left, right = sort(left), sort(right)    # 2. Sort each part recursively
    # 3. Merge 2 parts
    # return merge(left, right)
    """Wiki: Note that most worst-case sorting algorithms that do optimally well in the worst-case,
    notably heap sort and merge sort, do not take existing order within their input into account, 
    although this deficiency is easily rectified in the case of merge sort 
    by checking if the last element of the lefthand group is less than (or equal)
    to the first element of the righthand group, in which case a merge operation may be replaced by simple concatenation – 
    a modification that is well within the scope of making an algorithm adaptive.
    """
    # Here is this modification:
    if left[-1] > right[0]: 
        return merge(left, right)
    return left + right
