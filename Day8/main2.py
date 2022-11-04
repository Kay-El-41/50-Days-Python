def prime_numbers():
    num = int(input("Enter a number (integer): "))
    prime_llist = []
    flag = False
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                flag = True
                break
        if not flag:
            prime_llist.append(i)
        flag = False
    return prime_llist


print(prime_numbers())