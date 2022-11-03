def string_range(num: int):
    number_string = "0"
    for i in range(1, num):
        number_string += f".{i}"
    return number_string


print(string_range(0))