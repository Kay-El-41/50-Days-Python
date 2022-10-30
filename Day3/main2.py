def lowercase_converter(name_list: list):
    """return a tuple of sorted lowercase names"""
    lower_case_names = []
    for name in name_list:
        if name.lower() == name:
            lower_case_names.append(name)
    lower_case_names_tuple = tuple(sorted(lower_case_names, reverse=True))
    return lower_case_names_tuple


names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
print(lowercase_converter(names))