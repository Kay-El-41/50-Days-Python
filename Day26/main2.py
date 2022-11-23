s = 'Hi my name is Richard'


def string_length(a: str):
    new_list = a.split(" ")
    new_dict = {i : len(i) for i in new_list}
    return new_dict


print(string_length(s))