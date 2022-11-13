import random


def user_name():
    name = input("Please enter your name: ")
    username = name[::-1] + str(random.randint(0, 9))
    return username


print(user_name())