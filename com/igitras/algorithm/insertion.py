# coding=utf-8
import time
from com.igitras.algorithm.libs import swap_element, random_list

__author__ = 'mason'


# 直接插入排序
def direct_insertion(list_to_sort):
    length = len(list_to_sort)
    index = 1
    while index < length:
        inner_index = index
        while inner_index >= 1:
            if list_to_sort[inner_index] < list_to_sort[inner_index - 1]:
                swap_element(list_to_sort, inner_index, inner_index - 1)
            else:
                break
            inner_index -= 1
        index += 1


list_to_sort = random_list(100000, 0, 10000)
print time.time()
direct_insertion(list_to_sort)
print time.time()
print list_to_sort
