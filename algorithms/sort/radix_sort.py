from typing import Union, List


def sort(arr: List[Union[int]]) -> List[Union[int]]:
    """Radix sort algorithm.
    O( ? )
    """

    def counting_sort():
        pass
    
    if not arr:
        return arr
    repetitions = len(str(max(arr)))
    for i in repetitions:
        counting_sort()