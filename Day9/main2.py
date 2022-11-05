def zeros_last(num: list):
    if 0 in num:
        for j in num:
            if j == 0:
                num.remove(j)
                num.append(0)
    else:
        num.sort()
    return num


num_list1 = [1, 4, 6, 0, 7, 0, 9]
num_list2 = [2, 1, 4, 7, 6]
print(zeros_last(num_list1))
