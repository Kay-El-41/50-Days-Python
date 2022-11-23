def difference(a, b) -> list:
    new_list_a = [i for i in a if i not in b]
    new_list_b = [i for i in b if i not in a]
    new_list = new_list_a + new_list_b
    return new_list


print(difference([1, 2, 4, 5, 6],  [1, 2, 5, 7, 9]))
