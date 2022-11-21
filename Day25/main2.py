def read_backwards(a: str):
    new_str_list = a.split(" ")[::-1]
    txt = ""
    for index in new_str_list:
        txt += index + " "
    return txt


print(read_backwards("the love is real"))
