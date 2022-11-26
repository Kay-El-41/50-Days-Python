def repeated_names(name_list: list):
    h_count = 0
    most_repeated_name = ""
    for n in name_list:
        if name_list.count(n) > h_count:
            h_count = name_list.count(n)
            most_repeated_name = n
    return most_repeated_name


name = ['John', 'Peter', 'John', 'Peter', 'Jones', 'Peter']
print(repeated_names(name))