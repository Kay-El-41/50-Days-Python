def index_position(a: str):
    lower_index_list = []
    for w in a:
        if w.islower():
            lower_index_list.append(a.index(w))
    return lower_index_list


print(index_position('LovE'))
