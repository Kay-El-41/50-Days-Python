def hide_password():
    password = input("Enter a password: ")
    hidden_password = ""
    for j in password:
        hidden_password += "*"
    print(hidden_password)
    print(f"The password is {len(hidden_password)} characters long.")


hide_password()

