def sex_count(person_list: list):
    """return the count of male and female"""
    filtered_list = [j.lower() for j in person_list]
    male_count = filtered_list.count('male')
    female_count = filtered_list.count('female')
    return [('Male', male_count), ('Female', female_count)]


students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
print(sex_count(students))
