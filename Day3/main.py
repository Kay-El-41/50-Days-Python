def register_check(students: dict):
    student_count = 0
    for i in students:
        if students[i] == "yes":
            student_count += 1
    return student_count


register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}

print(register_check(register))
