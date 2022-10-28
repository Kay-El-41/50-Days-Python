import math


def divide_or_square(num: int):
    if num % 5 == 0:
        return round(math.sqrt(num), 2)
    else:
        return round(num % 5, 2)


print(divide_or_square(int(input("Enter a number: "))))


