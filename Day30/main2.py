def sorted_names(names_list: list):
    temp = []
    new_names_list = []

    for name in names_list:
        temp_name = ""
        temp = name.split(" ")
        temp.reverse()
        for n in temp:
            if n != temp[len(temp)-1]:
                temp_name += n+" "
            else:
                temp_name += n

        new_names_list.append(temp_name)
    new_names_list.sort()
    return new_names_list


names = ['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown', 'Tom Cruise']
print(sorted_names(names))

