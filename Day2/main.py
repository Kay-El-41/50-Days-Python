def convert_add(string_list: list):
    num_list = [int(x) for x in string_list]
    return sum(num_list)


new_list = ['1', '3', '5']
print(convert_add(new_list))
