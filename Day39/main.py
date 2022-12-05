import random as rm
import string

alphabets = list(string.ascii_letters)
punctions = list(string.punctuation)
number_list = list(string.digits)

combined_list = alphabets + punctions + number_list


def generate_password():
    password = ""
    while True:
        user_choice = input("Choose your password type: (w)eak, (s)trong, (v)ery strong: ")
        if user_choice == 'w':
            char = 5
            break
        elif user_choice == 's':
            char = 8
            break
        elif user_choice == 'v':
            char = 12
            break
        else:
            print("Wrong choice")

    for j in range(0, char):
        password += rm.choice(combined_list)
    return password


print(generate_password())
