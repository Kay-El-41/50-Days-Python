user_data = {}


def create_user():
    user_data["name"] = input("What is your name?")
    user_data["age"] = input("What is your age?")
    user_data["password"] = input("What is your password?")

    print("User saved, Please login.")
    name = input("Please enter username")
    password = input("Please enter password")

    while True:
        if name == user_data["name"] and password == user_data["password"]:
            print("Logged in successfully")
            break
        else:
            print("Wrong password or username. Please try again.")


create_user()