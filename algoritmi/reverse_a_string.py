# noob way

def reverse(string):
    string = string.split()  # ni le trimite intr-o lista ca elemente individuale
    string.reverse()  # ne intoarce elementel
    return string


string = 'Marco Vinter are interviu la Amdaris'
print('Noob way: ', reverse(string))


# algo way

def reverse_algo(string):
    spaces = ['']
    lenght = len(string)
    index = 0
    words = []

    while index < lenght:
        if string[index] not in spaces:
            word_start = index
            while index < lenght and string[index] not in spaces:
                index += 1
            words.append(string[word_start:index])
        index += 1
    return "".join(reversed(string))  # sau cu reverse


print('Algo way:', reverse_algo(string))
