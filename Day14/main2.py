def your_salary():
    monthly_rate = 20
    overtime_rate = 25

    teacher_info = {
        "name": input("Enter the teacher's name: "),
    }

    while True:
        try:
            teacher_info["periods"] = int(input("Enter the periods taught: "))
            break
        except ValueError:
            print("Please enter period in number")

    if teacher_info["periods"] <= 100:
        teacher_info["salary"] = teacher_info["periods"] * monthly_rate
    else:
        teacher_info["overtime"] = teacher_info["periods"] - 100
        teacher_info["salary"] = (100 * monthly_rate) + (teacher_info["overtime"] * overtime_rate)

    print(f"Teacher: {teacher_info['name']}")
    print(f"Periods: {teacher_info['periods']}")
    print(f"Teacher: {teacher_info['salary']:,}")


your_salary()
