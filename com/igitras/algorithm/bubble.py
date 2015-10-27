# coding=utf-8
from com.igitras.algorithm.libs import swap_element, random_list, validate_list_sorted

__author__ = 'mason'


# listToSort待排序数组, sort排序方式,True代表升序
def bubble(list_to_sort, sort):
    length = len(list_to_sort)

    index = length - 1
    while index > 0:
        for i in range(index):
            if list_to_sort[index] < list_to_sort[i]:
                swap_element(list_to_sort, i, index)
        index -= 1

    if not sort:
        list_to_sort.reverse()


listToSort = random_list(20, 0, 50)
bubble(listToSort, False)
validate_list_sorted(listToSort, False)
print listToSort
bubble(listToSort, True)
print listToSort
