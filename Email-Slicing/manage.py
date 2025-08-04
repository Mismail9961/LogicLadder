def email_slicer():
    print("Welcome to the email slicer")
    email = input("Enter your email address: ")
    username = email[:email.index("@")]
    domain = email[email.index("@")+1:]
    print(f"Your username is {username} and your domain is {domain}")

email_slicer()