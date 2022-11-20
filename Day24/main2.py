def nested_list(*list_group: list):
    n_list = []
    for li in list_group:
        n_list.append(li)
    return n_list


print(nested_list([1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]))
