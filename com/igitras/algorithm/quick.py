# coding=utf-8
from random import Random
from com.igitras.algorithm.libs import swap_element, random_list, validate_list_sorted

__author__ = 'mason'


# 快速排序
def quick_sort(list_to_sort, start, end):
    # 如果start和end一样，说明只有一个元素，就不需要再调整
    print list_to_sort, start, end
    if start >= end:
        return
    else:
        pivot_index = start
        left = start + 1
        right = end
        if left != right:
            while left < right:
                # 从右往左找到第一个小于pivot的数
                while right > left:
                    if list_to_sort[right] < list_to_sort[pivot_index]:
                        swap_element(list_to_sort, pivot_index, right)
                        pivot_index = right
                        break
                    else:
                        right -= 1
                # 从左往右找到第一个大于pivot的数
                while right > left:
                    if list_to_sort[left] > list_to_sort[pivot_index]:
                        swap_element(list_to_sort, pivot_index, left)
                        pivot_index = left
                        break
                    else:
                        left += 1
        else:
            if list_to_sort[pivot_index] > list_to_sort[left]:
                swap_element(list_to_sort, pivot_index, left)
            pivot_index = left
        quick_sort(list_to_sort, start, pivot_index - 1)
        quick_sort(list_to_sort, pivot_index + 1, end)


def quick_sort_with_order(list_to_sort, sort):
    quick_sort(list_to_sort, 0, len(list_to_sort) - 1)

    if not sort:
        list_to_sort.reverse()


listToSort = [9, 7, 3, 1, 1, 8, 7, 7]
print listToSort
quick_sort_with_order(listToSort, False)
validate_list_sorted(listToSort, False)
print listToSort

test_count = 100
random = Random()
while test_count > 0:
    test_count -= 1
    listToSort = random_list(random.randint(1, 10), 1, 10)
    print listToSort
    quick_sort_with_order(listToSort, False)
    validate_list_sorted(listToSort, False)
    print listToSort
