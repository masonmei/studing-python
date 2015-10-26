# coding=utf-8

__author__ = 'mason'


# listToSort待排序数组, sort排序方式,True代表升序
def bubble(list_to_sort, sort):
    length = len(list_to_sort)

    index = length - 1
    while index > 0:
        for i in range(index):
            if list_to_sort[index] < list_to_sort[i]:
                temp = list_to_sort[index]
                list_to_sort[index] = list_to_sort[i]
                list_to_sort[i] = temp
        index -= 1

    if not sort:
        list_to_sort.reverse()


listToSort = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
bubble(listToSort, False)
print listToSort
bubble(listToSort, True)
print listToSort
