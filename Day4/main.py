def only_floats(a, b):
    """ returns the number of floats"""
    if isinstance(a, float) and isinstance(b, float):
        return 2
    elif isinstance(a, float) or isinstance(b, float):
        return 1
    else:
        return 0


print(only_floats(12.1, 23))
