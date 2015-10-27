# coding=utf-8
__author__ = 'mason'


# 快速排序
def quick_sort(list_to_sort, start, end):
    left_pointer = start + 1
    right_pointer = end
    base_num = list_to_sort[start]

    if left_pointer > end:
        return

    while right_pointer > left_pointer:
        while base_num <= list_to_sort[right_pointer] and right_pointer > left_pointer:
            right_pointer -= 1
        while base_num >= list_to_sort[left_pointer] and right_pointer > left_pointer:
            left_pointer += 1
        if right_pointer > left_pointer:
            temp = list_to_sort[left_pointer]
            list_to_sort[left_pointer] = list_to_sort[right_pointer]
            list_to_sort[right_pointer] = temp

    tmp = list_to_sort[left_pointer]
    list_to_sort[left_pointer] = list_to_sort[start]
    list_to_sort[start] = tmp

    quick_sort(list_to_sort, start, left_pointer - 1)
    quick_sort(list_to_sort, right_pointer + 1, end)


def quick_sort_with_order(list_to_sort, sort):
    quick_sort(list_to_sort, 0, len(list_to_sort) - 1)

    if not sort:
        list_to_sort.reverse()


listToSort = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
quick_sort_with_order(listToSort, False)
print listToSort

listToSort = [6, 1, 2, 7, 9, 3, 4, 5, 10]
quick_sort_with_order(listToSort, True)
print listToSort
