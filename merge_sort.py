"""
This module contains merge sort.
"""


import random


def merge_sort(array):
    """
    Merge sort algorithm.
    """
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        left_index = 0
        right_index = 0
        main_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                array[main_index] = left[left_index]
                left_index += 1
            else:
                array[main_index] = right[right_index]
                right_index += 1
            main_index += 1

        while left_index < len(left):
            array[main_index] = left[left_index]
            left_index += 1
            main_index += 1

        while right_index < len(right):
            array[main_index] = right[right_index]
            right_index += 1
            main_index += 1

    return array


def merge_sort_comparisions(array, comparisions=0):
    """
    Merge sort algorithm.
    """

    if len(array) > 1:
        comparisions += 1
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort_comparisions(left, comparisions)
        merge_sort_comparisions(right, comparisions)

        left_index = 0
        right_index = 0
        main_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                array[main_index] = left[left_index]
                left_index += 1
            else:
                array[main_index] = right[right_index]
                right_index += 1
            comparisions += 3
            main_index += 1

        comparisions += 2

        while left_index < len(left):
            comparisions += 1
            array[main_index] = left[left_index]
            left_index += 1
            main_index += 1

        comparisions += 1

        while right_index < len(right):
            comparisions += 1
            array[main_index] = right[right_index]
            right_index += 1
            main_index += 1

        comparisions += 1

    comparisions += 1

    return comparisions
