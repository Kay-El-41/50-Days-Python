def swap_values(num: list):
    a = num[0]
    b = num[len(num)-1]
    num[0] = b
    num[len(num)-1] = a
    return num


print(swap_values([2, 4, 67, 7]))

