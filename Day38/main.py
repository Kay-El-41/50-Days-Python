import random as rm


def guess_a_number():
    random_number = rm.randrange(0, 100)
    print(random_number)
    life = 3

    while life > 0:
        user_guess = int(input("Guess a number within 0 to 100:"))
        if user_guess < random_number:
            life -= 1
            print("Too Low")
        elif user_guess > random_number:
            life -= 1
            print("Too High")
        else:
            return print("You Win")
    if life == 0:
        return print("You Lose")


guess_a_number()
