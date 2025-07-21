#String Basic : 
name = input("Enter your Name : ")
print(name.upper())
print(name.lower())
print(len(name))
print(name[0])
print(name[-1])


#String Slicing : 
text = "Hello World!"
print(text[0:5])
print(text[:5])
print(text[6:])
print(text[::-1])


#f-strings (formatted strings) : 
name = "Ismail"
age = 18
print(f"My name is {name} and I am {age} years old.")


#Numbers and Arithmetic : 
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3  (floor division)
print(a % b)   # 1  (modulus)
print(a ** b)  # 1000 (exponentiation)

#Comparison Operators : 
print(5 == 5)    # True
print(5 != 3)    # True
print(5 > 3)     # True
print(5 < 3)     # False
print(5 >= 5)    # True
print(5 <= 4)    # False

#💻 Mini Project: Quote Formatter
quote = input("Enter Your Quote : ")
Author = input("Enter your AUTHOR Name : ")

print("\nHhere is your Formated Quote : \n")
print(f'"{quote}"')
print(f" -{Author}")