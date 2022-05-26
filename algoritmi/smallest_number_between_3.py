def small_of_3(a, b, c):
    print('a:', a, '\nb:', b, '\nc:', c)
    if a < b and a < c:
        print("--> a is the smallest number")
    if b < a and b < c:
        print('--> b is the smallest number')
    if c < a and c < b:
        print('--> c is the smallest number')


small_of_3(5, 1, 3)
