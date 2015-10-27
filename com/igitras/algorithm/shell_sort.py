# coding=utf-8
from random import Random
import time
from com.igitras.algorithm.libs import random_list, validate_list_sorted, swap_element

__author__ = 'mason'


# 希尔排序
def shell_sort(list_to_sort):
    length = len(list_to_sort)

    dist = length / 2

    while dist > 0:
        for i in range(dist, length):
            j = i
            while j >= dist and list_to_sort[j] <= list_to_sort[j - dist]:
                swap_element(list_to_sort, j, j - dist)
                j -= dist

        dist /= 2


test_count = 100
random = Random()
while test_count > 0:
    test_count -= 1
    arr_to_sort = random_list(random.randint(1, 10), 1, 10)
    shell_sort(arr_to_sort)
    print arr_to_sort
    validate_list_sorted(arr_to_sort)

# arr_to_sort = random_list(100000, 0, 10000)
# print arr_to_sort
#
# print time.time()
# shell_sort(arr_to_sort)
# print time.time()
# validate_list_sorted(arr_to_sort, True)
# print arr_to_sort
