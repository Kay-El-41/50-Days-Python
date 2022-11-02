def user_name():
    email = input("Enter your email address: ")
    username = email.split("@")[0]
    return username


print(user_name())
