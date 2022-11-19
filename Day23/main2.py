s = "love live and laugh"


def multiply_words(a: str):
    str_list = a.split(" ")
    mul = 1
    text_to_p = ""
    for word in str_list:
        mul *= len(word)
        text_to_p += f"{word}({len(word)}) "

    print(f"{mul} - {text_to_p}")


multiply_words(s)