def sort_words(a: str):
    new_list = a.split(" ")
    alpha_list = []

    for w in new_list:
        for index in w:
            alpha_list.append(index)

    alpha_set = set(alpha_list)
    alpha_list = list(alpha_set)
    alpha_list.sort()

    entry = alpha_list[0]
    for i in range(1, len(alpha_list)):
        entry += "," + alpha_list[i]
    return [entry]


print(sort_words("love life"))


