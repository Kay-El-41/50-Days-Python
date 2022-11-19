def add(a, b):
    return a+b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b


operator_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}

try:
    n1 = float(input("Enter first number: "))
except ValueError:
    print("Should Be Number Only")

while True:
    try:
        op = input("Enter operator +, - , * , /: ")
        n2 = float(input("Enter second number: "))

        if op in operator_functions:
            n3 = operator_functions[op](n1, n2)
            print(n3)
            if input(f"Continue with {n3}? Y/N/C") == "Y":
                n1 = n3
            else:
                n1 = float(input("Enter first number: "))
        else:
            print("Wrong Operator.")

    except ValueError:
        print("Should Be Number Only")

    except ZeroDivisionError:
        print("Second Number Must Not Be Zero")



