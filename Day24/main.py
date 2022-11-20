def average_calories():
    calories_per_day = []
    while True:
        a = int(input("Enter calories: "))
        calories_per_day.append(a)
        if input("Quit? Y : ") == "Y":
            break
    return sum(calories_per_day) / len(calories_per_day)


print(average_calories())
