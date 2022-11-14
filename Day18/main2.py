def add_reverse(a: list, b: list):
    if len(a) != len(b):
        return "The lists are not of equal lengths."
    else:
        new_list = []
        for n in range(0, len(a)):
            new_list.append(a[n]+b[n])
        new_list.reverse()
        return new_list


print(add_reverse([10, 12, 34], [12, 56, 78]))
