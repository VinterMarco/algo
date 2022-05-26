def biggest_number_in_a_list(lst):
    biggest = lst[0]
    for i in range(len(lst)):
        if biggest < lst[i]:
            biggest = lista[i]
    print(biggest)


lista = [2, 5, 10, 11, -50]
biggest_number_in_a_list(lista)
