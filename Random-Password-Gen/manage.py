import random
import string

def generate_password():
    length = int(input("Enter the length of the password: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(password)

option = input("Do you want to generate a password? (y/n): ")
if option == "y":
    generate_password()
else:
    print("Thank you for using the password generator")