def largest_number(a: list):
    numbers_text = ""
    numbers_list = []
    for num in a:
        numbers_text += str(num)
    for n in numbers_text:
        numbers_list.append(n)
    numbers_list.sort(reverse=True)

    new_text = ""
    for num in numbers_list:
        new_text += num

    return format(format(int(new_text), ","))


list1 = [3, 67, 87, 9, 2]
print(largest_number(list1))
