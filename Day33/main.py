def inter_section(a, b):
    intersect_list = [n for n in a if n in b]
    return intersect_list




list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]

print(inter_section(list1, list2))