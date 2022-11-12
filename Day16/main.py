def sum_list(item: list):
    total = 0
    for i in item:
        if type(i) is list:
            total += sum(i)
    return total


print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))
