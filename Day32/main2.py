valid_requirements = ["@", ".", "com"]


# def email_validator(em: list):
#     valid_emails = []
#     for item in em:
#         count = 0
#         for ev in valid_requirements:
#             if ev in item:
#                 count += 1
#             if count == 3:
#                 if item.index("@") != 0:
#                     valid_emails.append(item)
#     return valid_emails

def email_validator(arr: list):
    valid_emails = []
    for email in arr:
        if "@" in email and email.count('@') == 1 and email[-4:] == '.com':
            if email[0] != '@':
                valid_emails.append(email)
        # Checking if list with emails is empty.
        elif len(valid_emails) == 0:
            return 'All emails are invalid'
    return f'The list of valid emails is: {valid_emails}'


emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@mail.com']
print(email_validator(emails))
