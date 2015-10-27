# coding=utf-8
__author__ = 'mason'

from random import Random


# 交换数组中的两个元素
def swap_element(elements_list, from_index, to_index):
    length = len(elements_list)
    if length < from_index or length < to_index:
        raise Exception("invalid swap element index.")

    tmp = elements_list[from_index]
    elements_list[from_index] = elements_list[to_index]
    elements_list[to_index] = tmp


def random_list(size, min=0, max=1000):
    random = Random()
    result = []
    count = size
    while count > 0:
        result.append(random.randint(min, max))
        count -= 1
    return result


def validate_list_sorted(list_sorted, order=True):
    length = len(list_sorted)
    if length > 1:
        while length > 1:
            if order:
                if list_sorted[length - 1] < list_sorted[length - 2]:
                    print list_sorted
                    raise Exception("not sorted in asc")
            else:
                if list_sorted[length - 1] > list_sorted[length - 2]:
                    print list_sorted
                    raise Exception("not sorted in desc")
            length -= 1
