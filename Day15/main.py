def same_in_reverse(txt: str):
    reversed_txt = txt[::-1]
    if txt.lower() == reversed_txt.lower():
        return True
    else:
        return False


print(same_in_reverse("dad"))

