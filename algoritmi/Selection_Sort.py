"""
Definitie:
Selection Sort works by finding
the smallest element (in case of ascending order)
or the largest element (in case of descending order)
and placing them in the first position.
It then omits the first element and repeats
the process with the leftover array and places
the next smallest or largest element in the second position.
This process continues until all elements in the array have
been sorted into their proper positions.

"""


def selection_sort(arr):  # define the function
    for i in range(len(arr)):
        min = i  # setting the first element as the minimum
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:  # compare to find smallest
                min = j  # set the smallest as the min
        arr[i], arr[min] = arr[min], arr[i]  # swap the first element and the min
        print(arr)  # display the array at each step

lst = [5, 1, 7, 4, 10, 23, 99, 8, 22, 32, 15]

print(selection_sort(lst))