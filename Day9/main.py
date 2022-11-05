def biggest_odd(num: str):
    numbers = [int(a) for a in num if int(a) % 2 != 0]
    return max(numbers)


print(biggest_odd("23569"))

