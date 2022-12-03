vowels = ['a', 'e', 'i', 'o', 'u']


def count_the_vowels(a: str):
    vw_contained = []
    for w in a:
        if w in vowels:
            vw_contained.append(w)
    vw = list(set(vw_contained))
    return len(vw)


print(count_the_vowels('sass'))


