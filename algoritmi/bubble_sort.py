"""
definitie:
works by comparing adjacent values
in the list and places them in the
correct order. It then continues
to do that throughout the list
over and over again until all
the values in the list have been arranged
in the preferred order
"""


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


lst = [5, 1, 7, 4, 10, 23, 99, 8, 22, 32, 15]
print(bubble_sort(lst))