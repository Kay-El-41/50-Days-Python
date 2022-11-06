def convert_numbers(figures: list):
    new_list = []
    for num in figures:
        new_list.append(f"{num:,}")
    return new_list


figures_list = [1000000, 2356989, 2354672, 9878098]
print(convert_numbers(figures_list))
