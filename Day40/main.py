a = 'i love you'
vowels = ['a', 'e', 'i', 'o', 'u']


def translate(text: str):
    output = []
    for j, word in enumerate(a.split()):
        if word[0] in vowels:
            output.append(word[j] + 'yay')
        else:
            output.append(word[1:] + word[0] + 'ay')
    return ' '.join(output)


print(translate(a))