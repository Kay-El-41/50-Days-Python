upper_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y','Z']
strl = 'leArning is hard, bUt if You appLy youRself \ you can achieVe success'

word_list = strl.split(" ")
new_list = []

for word in word_list:
    for w in word:
        if w in upper_alphabets:
            new_list.append(word[::-1])

new_set = set(new_list)
new_list = list(new_set)

print(new_list)

