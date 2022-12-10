def email_validator(arr: list):
    valid_emails = []
    for email in arr:
        if "@" in email and email.count('@') == 1 and email[-4:] == '.com':
            if email[0] != '@':
                valid_emails.append(email)
        # Checking if list with emails is empty.
    return valid_emails


def save_emails():
    emails = []
    while True:
        user_input = input("Enter a Email: (done)?: ")
        if user_input.lower() == 'done':
            break
        else:
            emails.append(user_input)

    v_emails = email_validator(emails)
    with open('emails.csv', 'a') as file:
        for mail in v_emails:
            file.writelines(mail + "\n")


def open_emails():
    with open('emails.csv', 'r') as file:
        return_list =  file.readlines()
        new_list = [mail[:-1] for mail in return_list]
        return new_list


save_emails()
print(open_emails())
