def missing_numbers(a: list):
    missing_list = []
    for j in range(a[0], a[-1] + 1):
        if j not in a:
            missing_list.append(j)
    return missing_list


list1 = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
print(missing_numbers(list1))
