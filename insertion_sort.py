"""
This module contains insertion sort.
"""


def insertion_sort(array):
    """
    Insertion sort algorithm.
    """
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition - 1]
            currentPosition = currentPosition - 1

        array[currentPosition] = currentValue

    return array


def insertion_sort_comparisions(array):
    """
    Insertion sort algorithm.
    """
    comparisions = 0
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            comparisions += 2
            array[currentPosition] = array[currentPosition - 1]
            currentPosition = currentPosition - 1

        comparisions += 2
        array[currentPosition] = currentValue

    return comparisions
