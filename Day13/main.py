def your_vat():
    while True:
        try:
            price = float(input("Enter the produce price: $"))
            vat = float(input("Enter the product price: %"))
            break
        except ValueError:
            print("Please Enter Numbers Only.")

    tax_included = price + (price * vat / 100)
    return round(tax_included)


print(f"Your final price is ${your_vat()}.")

