import string

alphabet = list(string.ascii_lowercase)


def check_pangram(a: str):
    for letter in alphabet:
        if letter not in a:
            return False
    return True


str = "the quick brown fox jumps over the lazy dog"
print(check_pangram(str))
