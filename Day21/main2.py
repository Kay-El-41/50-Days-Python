def even_or_average():
    num_list = []
    for j in range(0, 5):
        num_list.append(int(input("Enter a number: ")))

    largest_even = 0
    even_count = 0

    for num in num_list:
        if num % 2 == 0:
            even_count += 1
            if num > largest_even:
                largest_even = num
    if even_count > 0:
        return largest_even
    else:
        return sum(num_list) / len(num_list)


print(even_or_average())
