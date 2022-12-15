def search_binary(list1: list, x):
    low = 0
    high = len(list1) - 1
    mid_index = 0

    while low <= high:
        mid_index = (high + low) // 2

        if list1[mid_index] == x:
            return mid_index

        # if an element is lower than the middle index
        # then search the lower part of the list

        elif list1[mid_index] > x:
            high = mid_index - 1

        # if an element is higher than the middle index
        # then search the higher part of the list

        elif list1[mid_index] < x:
            low = mid_index + 1

    return 'no element'


num_list = [12, 34, 56, 78, 98, 22, 45, 13]
sorted_list1 = sorted(num_list)
number = 22

result = search_binary(sorted_list1, number)
if result == 'no element':
    print(f"There is no {number} in list")
else:
    print(f"The element index is {result}.")


