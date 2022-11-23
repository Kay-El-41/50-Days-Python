def unique_numbers(a: list):
    unique_list = list(set(a))
    if (sum(a) - sum(unique_list)) % 2 == 0:
        return a
    else:
        return unique_list


print(unique_numbers([1, 2, 4, 5, 6, 7, 8, 8]))
