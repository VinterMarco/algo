"""  definitie :

Linear search works by starting from the
0th element and comparing the user’s input element
with each term and finally returning
the position of the element.  """

# linear search function
def linear_search(lista, x):
    for index in range(len(lista)):
        if lista[index] == x:
            return index

    return -1


# calling the function
lst = [5, 1, 7, 4, 10, 23, 99, 8, 22, 32, 15]
numar = 333

print(linear_search(lst, numar))
