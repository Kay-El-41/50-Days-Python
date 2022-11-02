def zeroed(num_list: list):
    num_list[0] = 0
    num_list[len(num_list)-1] = 0
    return num_list


number_list = [2, 5, 7, 8, 9]
print(zeroed(number_list))
