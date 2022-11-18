def make_tuples(a: list, b: list):
    new_list = []
    if len(a) == len(b):
        for j in range(0, len(a)):
            new_tupl = (a[j], b[j])
            new_list.append((new_tupl))
        print (new_list)
    else:
        print("Wrong length of list.")


make_tuples([1, 2, 3, 4], [5, 6, 7, 8])

