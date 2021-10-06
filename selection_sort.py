"""
This module contains selection sort.
"""


def selection_sort(array):
    """
    Selection sort algorithm.
    """
    array_lenth = len(array)

    for index in range(array_lenth):
        min_index = index

        for smallest in range(index + 1, array_lenth):

            if array[smallest] < array[min_index]:
                min_index = smallest

        array[index], array[min_index] = array[min_index], array[index]

    return array


def selection_sort_comparisions(array):
    """
    Selection sort algorithm.
    """
    array_lenth = len(array)
    comparisons = 0

    for index in range(array_lenth):
        min_index = index

        for smallest in range(index + 1, array_lenth):

            if array[smallest] < array[min_index]:
                min_index = smallest
            comparisons += 1

        array[index], array[min_index] = array[min_index], array[index]

    return comparisons
