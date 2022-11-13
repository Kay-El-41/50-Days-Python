names = ["Peter", "Jon", "Andrew"]


def sort_length(names_list: list):
    new_list = []
    for n in names_list:
        more_count = 0
        for j in range(0, len(names_list) - 1):
            if len(n) > len(names_list[j]):
                more_count += 1
        new_list.insert(more_count, n)
    print(new_list)


sort_length(names)

