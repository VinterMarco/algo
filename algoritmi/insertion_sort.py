"""
definitie:

sorts the adjacent elements, reaches
the last element, and then starts
at the first element again to repeatedly
go through this process and sort the complete
array, insertion sort starts at the first
element and as it moves towards the last
element, sorts all the elements that it passes.

"""


def insertion_sort(arr):  # define the Insertion Sort function
    for i in range(len(arr)):
        j = i  # start at the last element of the sub-array
        while j != 0 and arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j = j - 1  # go down from i to 0 in the sub-array while sorting it
        print(arr)  # we place it in the loop to display each step


lst = [5, 1, 7, 4, 10, 23, 99, 8, 22, 32, 15, 5, 1, 7, 4, 10, 23, 99, 8, 22, 32, 15, ]
insertion_sort(lst)
