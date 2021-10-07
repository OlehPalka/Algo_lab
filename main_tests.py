import matplotlib.pyplot as plt
import json
from array import array
from selection_sort import *
from insertion_sort import *
from merge_sort import *
from shell_sort import *
import random
from timeit import default_timer as timer

import copy


def first_condition(sort_func, sort_func_compar):
    """
    випадковим чином згенерований масив (згенерувати 5 експериментів та записати середнє значення)
    """

    dict_of_time = {}
    dict_of_comp = {}

    for power in range(7, 16):
        list_of_time = []
        list_of_comp = []

        for _ in range(5):
            array = [random.random() for _ in range(2 ** power)]
            array_copy = copy.deepcopy([random.random()
                                        for _ in range(2 ** power)])
            start = timer()
            sort_func(array)
            algoritm_time = timer() - start

            list_of_time.append(algoritm_time)
            list_of_comp.append(sort_func_compar(array_copy))

        avarage_time = sum(list_of_time) / 5
        avarage_comp = sum(list_of_comp) / 5

        dict_of_time["2 ** " + str(power)] = avarage_time
        dict_of_comp["2 ** " + str(power)] = avarage_comp
    return dict_of_time, dict_of_comp


def second_condition(sort_func, sort_func_compar):
    """
    значення масиву відсортовані у порядку зростання;
    """
    dict_of_time = {}
    dict_of_comp = {}

    for power in range(7, 16):

        array = [num for num in range(2 ** power)]
        array_copy = copy.deepcopy([num for num in range(2 ** power)])
        start = timer()
        sort_func(array)
        algoritm_time = timer() - start

        dict_of_time["2 ** " + str(power)] = algoritm_time
        dict_of_comp["2 ** " + str(power)] = sort_func_compar(array_copy)
    return dict_of_time, dict_of_comp


def third_condition(sort_func, sort_func_compar):
    """
    значення масиву відсортовані у порядку зменшення
    """
    dict_of_time = {}
    dict_of_comp = {}

    for power in range(7, 16):

        array = [num for num in range(2 ** power)]
        array_copy = copy.deepcopy([num for num in range(2 ** power)])
        array.reverse()
        array_copy.reverse()

        start = timer()
        sort_func(array)
        algoritm_time = timer() - start

        dict_of_time["2 ** " + str(power)] = algoritm_time
        dict_of_comp["2 ** " + str(power)] = sort_func_compar(array_copy)
    return dict_of_time, dict_of_comp


def fourth_condition(sort_func, sort_func_compar):
    """
    масив містить лише елементи з множини {1, 2, 3} - тобто в масиві багато елементів,
    які повторюються; згенерувати 3 експерименти 
    (шляхом перестановки значень масивів) та записати середнє значення.
    """

    dict_of_time = {}
    dict_of_comp = {}

    for power in range(7, 16):
        list_of_time = []
        list_of_comp = []

        for _ in range(3):
            array = [random.choice([1, 2, 3]) for _ in range(2 ** power)]
            array_copy = copy.deepcopy(
                [random.choice([1, 2, 3]) for _ in range(2 ** power)])
            start = timer()
            sort_func(array)
            algoritm_time = timer() - start

            list_of_time.append(algoritm_time)
            list_of_comp.append(sort_func_compar(array_copy))

        avarage_time = sum(list_of_time) / 3
        avarage_comp = sum(list_of_comp) / 3
        dict_of_time["2 ** " + str(power)] = avarage_time
        dict_of_comp["2 ** " + str(power)] = avarage_comp

    return dict_of_time, dict_of_comp


def show_graphic():
    with open('tests.json') as file:
        tests = json.load(file)
    print("Enter a number of the experement of which you want to see the graph.")
    experement = int(input("Possible variants to choose: 1, 2, 3, 4: "))
    while experement not in [1, 2, 3, 4]:
        print("You have entered a wrong number")
        print("Try again!")
        experement = int(input("Possible variants to choose: 1, 2, 3, 4: "))

    task = ["First condition", "Second condition",
            "Third condition", "Fourth condition"][experement - 1]

    selection_time = list(tests["Selection sort"]
                          [task]["Time"].values())
    insertion_time = list(tests["Insertion sort"]
                          [task]["Time"].values())
    merge_time = list(tests["Merge sort"]
                      [task]["Time"].values())
    shell_time = list(tests["Shell sort"]
                      [task]["Time"].values())
    selection_comp = list(tests["Selection sort"]
                          [task]["Comparisions"].values())
    insertion_comp = list(tests["Insertion sort"]
                          [task]["Comparisions"].values())
    merge_comp = list(tests["Merge sort"]
                      [task]["Comparisions"].values())
    shell_comp = list(tests["Shell sort"]
                      [task]["Comparisions"].values())
    powers_list = [7, 8, 9, 10, 11, 12, 13, 14, 15]

    plt.figure("Algorithms time")
    plt.plot(powers_list, selection_time, label='Selection sort')
    plt.plot(powers_list, insertion_time, label="Insertion sort")
    plt.plot(powers_list, merge_time, label="Merge sort")
    plt.plot(powers_list, shell_time, label="Shell sort")
    plt.legend()
    plt.ylabel("Time")
    plt.xlabel("Power of 2")
    plt.yscale("log", base=10)

    plt.figure("Algorithms comparisons")
    plt.plot(powers_list, selection_comp, label='Selection sort')
    plt.plot(powers_list, insertion_comp, label="Insertion sort")
    plt.plot(powers_list, merge_comp, label="Merge sort")
    plt.plot(powers_list, shell_comp, label="Shell sort")
    plt.legend()
    plt.ylabel("Comparisions amount")
    plt.xlabel("Power of 2")
    plt.yscale("log", base=10)
    plt.show()


if __name__ == "__main__":
    # print("start")
    # tests = {}
    # for str_function, sort, comparisions_func in [("Selection sort", selection_sort, selection_sort_comparisions), ("Insertion sort", insertion_sort, insertion_sort_comparisions), ("Merge sort", merge_sort, merge_sort_comparisions), ("Shell sort", shell_sort, shell_sort_comparisions)]:
    #     tests[str_function] = {}
    #     for task, function in [("First condition", first_condition), ("Second condition", second_condition), ("Third condition", third_condition), ("Fourth condition", fourth_condition)]:
    #         algo_time, algo_comp = function(sort, comparisions_func)
    #         tests[str_function][task] = {
    #             "Time": algo_time, "Comparisions": algo_comp}
    # file = open('tests.json', 'w')
    # json.dump(tests, file)
    # file.close()
    show_graphic()
