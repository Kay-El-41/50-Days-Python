def all_the_same(item):
    new_set = set(item)
    if len(new_set) == 1:
        return True
    else:
        return False


print(all_the_same(['Mary', 'Mary', 'Mary']))