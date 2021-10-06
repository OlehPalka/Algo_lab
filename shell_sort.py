"""
This module contains shell sort.
"""


import random


def shell_sort(array):
    """
    This is shell sort algorithm.
    """
    lenth = len(array)
    step = 1

    while step < lenth // 3:
        step = 3 * step + 1

    while step >= 1:

        for iterator in range(step, lenth):
            help_iterator = iterator

            while help_iterator >= step and array[help_iterator] < array[help_iterator-step]:
                array[help_iterator], array[help_iterator -
                                            step] = array[help_iterator-step], array[help_iterator]
                help_iterator -= step
        step //= 3

    return array


def shell_sort_comparisions(array):
    """
    Shell sort algorithm.
    """
    comparisions = 0

    lenth = len(array)
    step = 1

    while step < lenth // 3:
        comparisions += 1
        step = 3 * step + 1

    comparisions += 1

    while step >= 1:
        comparisions += 1

        for iterator in range(step, lenth):
            help_iterator = iterator

            while help_iterator >= step and array[help_iterator] < array[help_iterator-step]:
                comparisions += 2
                array[help_iterator], array[help_iterator -
                                            step] = array[help_iterator-step], array[help_iterator]
                help_iterator -= step

            comparisions += 2

        step //= 3

    comparisions += 1

    return comparisions
