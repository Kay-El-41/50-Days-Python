def my_discount():
    price = int(input("Enter the product original price: "))
    discount = int(input("Enter the discount(%): "))

    disounted_price = price - ((discount*price)/100)
    return disounted_price


print(my_discount())
