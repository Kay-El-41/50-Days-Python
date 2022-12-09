def student_marks():
    students = {}
    while True:
        name = input("What is student name: (done?): ")
        if name.lower() == "done":
            break
        else:
            mark = input("Enter student mark: ")
            students[name] = mark
    return students


print(student_marks())
