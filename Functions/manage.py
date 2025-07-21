# #Defining Functions
# def greet():
#     print("Hello!")

# #Parameters and Arguments
# def greet(name):
#     print(f"Hello, {name}!")
# greet("Ismail")

# #Return Values
# def add(a, b):
#     return a + b
# result = add(3, 5)
# print(result)  # 8

# #Scope (Local vs Global)
# x = 10  # global

# def show():
#     x = 5  # local
#     print("Inside:", x)

# show()
# print("Outside:", x)

# #Practice Problem:
# #P1
# def is_palindrome(text):
#     return text == text[::-1]

# print(is_palindrome("madam"))  # True
# print(is_palindrome("hello"))  # False

# #P2
# def fibonacci(n):
#     sequence = [0, 1]
#     for i in range(2, n):
#         sequence.append(sequence[-1] + sequence[-2])
#     return sequence[:n]

# print(fibonacci(10))

def lenght_converter():
    print("Conver Lenght : ")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    choice = int(input("Enter your Choice"))

    if choice == 1 :
        meters = float(input("Meters :"))
        print(f"{meters} meters = {meters * 3.28084} feet")
    elif choice == 2:
        feet = float(input("Feet: "))
        print(f"{feet} feet = {feet / 3.28084} meters")
    else:
        print("Invalid choice")

def weight_converter():
    print("Convert weight:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        kg = float(input("Kilograms: "))
        print(f"{kg} kg = {kg * 2.20462} lbs")
    elif choice == 2:
        lbs = float(input("Pounds: "))
        print(f"{lbs} lbs = {lbs / 2.20462} kg")
    else:
        print("Invalid choice")

def main():
    print("Unit Converter")
    print("1. Length")
    print("2. Weight")
    option = int(input("Choose converter: "))
    
    if option == 1:
        lenght_converter()
    elif option == 2:
        weight_converter()
    else:
        print("Invalid option")

main()