def password_validator():
    while True:
        password = input("Please enter a password")
        uppercase = 0
        lowercase = 0
        number = 0
        if len(password) >= 8:
            for a in password:
                if a.islower():
                    lowercase += 1
                if a.isupper():
                    uppercase += 1
                if a.isnumeric():
                    number += 1
            if uppercase > 0 and lowercase > 0 and number >0:
                print(password+" is valid.")
                break
            else:
                print("Please enter another password")
        else:
            print("Please enter another password")


password_validator()