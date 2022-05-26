# asa gasim numerele

def two_sum(nums, target):
    complementMap = dict()

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if num in complementMap:
            return [complementMap[num], num]
        else:
            complementMap[complement] = num


lista = [5, 1, 2, 3, 4, 5]
two_sum = two_sum(lista, 10)
print(two_sum)


# asa gasim indexul

def two_sum(nums, target):
    complementMap = dict()

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if num in complementMap:
            return [complementMap[num], i]
        else:
            complementMap[complement] = i


lista = [5, 1, 2, 3, 4, 5]
two_sum = two_sum(lista, 10)
print(two_sum)
