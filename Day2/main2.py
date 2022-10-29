def check_duplicates(string_list: list):
    duplicate_list = []
    for item in string_list:
        if string_list.count(item) > 1:
            if item not in duplicate_list:
                duplicate_list.append(item)

    if len(duplicate_list) > 0:
        return duplicate_list
    else:
        return "No Duplicates"


fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

print(check_duplicates(fruits))
