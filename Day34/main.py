def just_digits(f_name: str):
    with open (f_name, 'r') as file:
        new_list = file.read().split(" ")
    digits = []
    for n in new_list:
        if n.isdigit():
            digits.append(n)
    return digits


print(just_digits('python.csv'))

