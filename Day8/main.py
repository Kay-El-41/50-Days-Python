def odd_even(numbers: list):
    even_numbers = [i for i in numbers if i % 2 == 0]
    odd_numbers = [i for i in numbers if i % 2 != 0]
    difference = max(even_numbers)-min(odd_numbers)
    return f"{max(even_numbers)}-{min(odd_numbers)}={difference}"


new_list = [1, 2, 4, 6]
print(odd_even(new_list))
