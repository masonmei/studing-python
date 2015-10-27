# coding=utf-8
import time
from com.igitras.algorithm.libs import swap_element, random_list, validate_list_sorted

__author__ = 'mason'


# 二分插入排序
def binary_search_sort(list_to_sort):
    length = len(list_to_sort)
    index = 1

    while index < length:

        left = 0
        right = index - 1

        while right >= left:
            mid = (left + right) / 2

            if list_to_sort[mid] <= list_to_sort[index]:
                left = mid + 1
            else:
                right = mid - 1

        # print left, right
        mid = left
        while mid < index:
            swap_element(list_to_sort, mid, index)
            mid += 1

        index += 1


arr_to_sort = random_list(100000, 0, 10000)
print arr_to_sort
print time.time()
binary_search_sort(arr_to_sort)
print time.time()
validate_list_sorted(arr_to_sort, True)
print arr_to_sort
