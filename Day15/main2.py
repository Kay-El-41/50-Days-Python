names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}


def your_age():
    name = input("Please Enter Your Name: ").lower()
    if name not in names_age.keys():
        print("Your name is not in the data base, it will be added")
        age = int(input("please Enter Your Age: "))
        names_age[name] = age
    print(f"Hi, {name.title()}, you are {names_age[name]} years old.")


your_age()
