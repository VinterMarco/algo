""" definitie:

While linear search compares the input
element with every element in the list
starting from the first element, the
binary search algorithm starts with the middle element.
"""


# binary search function

# Binary Search Function
def binary_search(arr, l, r, num):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            return binary_search(arr, l, mid - 1, num)
        else:
            return binary_search(arr, mid + 1, r, num)
    else:
        return -1


# Calling the function
arr = [1, 3, 4, 6, 7, 10, 22, 45, 49, 63, 78]
num = 10
print(binary_search(arr, 0, len(arr) - 1, num))
