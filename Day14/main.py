def flat_list(n_list: list):
    for item in n_list:
        if type(item) == list:
            print(item)


flat_list([[2, 4, 5, 6]])
