def words_with_vowels(str1: str):
    vow = []
    for j in str1.split():
        for k in j:
            if k in 'aeiou':
                vow.append(j)
                break
    return vow


print(words_with_vowels("You have no rhythm"))