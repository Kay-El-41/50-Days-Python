def longest_word(item: list):
    count = 0
    longest = ""
    for n in item:
        if len(n) > count:
            count = len(n)
            longest = n
    return [count, longest]

# def longest_word(a):
#     b = []
#     for word in a:
#         b.append([len(word), word])
#     return max(b)


print(longest_word(['Java', 'JavaScript', 'Python']))
