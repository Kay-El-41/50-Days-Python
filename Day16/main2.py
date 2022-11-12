nested_list = [[12, 34, 56, 67], [34, 68, 78]]


def num_picker(item: list):
    new_list = []
    for i in item:
        if 34 in i:
            new_list.append(34)
        if 67 in i:
            new_list.append(67)
        if 78 in i:
            new_list.append(78)
    final_list = list(set(new_list))
    return final_list


print(num_picker(nested_list))
