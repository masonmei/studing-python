# coding=utf-8
__author__ = 'mason'


# 直接插入排序
def direct_insertion(list_to_sort):
    length = len(list_to_sort)
    index = 1
    while index < length:
        inner_index = index
        while inner_index >= 1:
            if list_to_sort[inner_index] < list_to_sort[inner_index - 1]:
                tmp = list_to_sort[inner_index]
                list_to_sort[inner_index] = list_to_sort[inner_index - 1]
                list_to_sort[inner_index - 1] = tmp
            else:
                break
            inner_index -= 1
        index += 1


listToSort = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
direct_insertion(listToSort)
print listToSort
