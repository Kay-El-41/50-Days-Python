def equal_strings(a: str, b:str):
    if len(a) == len(b):
        for j in a:
            if j not in b:
                return False
        return True


print(equal_strings("love", "evol"))
