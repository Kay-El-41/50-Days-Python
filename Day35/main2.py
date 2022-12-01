def find_index(a_list: list, a_int: int):
    if a_int in a_list:
        index_list = [i for i, x in enumerate(a_list) if x == a_int]
    else:
        index_list = [a_int for j in a_list]
    return index_list


ls = [1, 2, 4, 6, 7, 7]

print(find_index(ls, 7))
print(find_index(ls, 8))
