import textblob


def spelling_checker():
    user_input = input("Enter a word: ")
    w = textblob.Word(user_input)
    if user_input != w.correct():
        user_asking = input("Are you sure? Y/N: ")
        if user_asking == "Y":
            return user_input
        else:
            return w.correct()
    else:
        return user_input


print(spelling_checker())


