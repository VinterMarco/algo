def smallest_from_a_list(lst):
    smallest = lst[0]
    for index in range(0, len(lst)):
        if smallest > lst[index]:
            smallest = lst[index]

    print(smallest)


lista = [10, 9, 8, 43, 34, 12, 543, 2, 5, 2.3, -2.3]
smallest_from_a_list(lista)
