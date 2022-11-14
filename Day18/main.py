def any_number(*nums):
    total = 0
    count = 0
    for num in nums:
        count += 1
        total += num
    return total/count


print(any_number(12, 90, 12, 34))


