def add_hash(a: str):
    b = a.replace(" ", "#")
    return b


def add_underscore(a: str):
    b = a.replace("#", "_")
    return b


def remove_underscore(a: str):
    b = a.replace("_", " ")
    return b


print(remove_underscore(add_underscore(add_hash('Python is Great'))))
