def longest_value(a: dict):
    length = 0
    for i in a:
        if len(a[i]) > length:
            longest = a[i]
            length = len(a[i])
    return longest


new_dict = {
    'fruit': 'apple',
    'color': 'red',
    'taste': 'sweet',
    'variation color': 'green',
}

print(longest_value(new_dict))
