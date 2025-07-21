a = int(input("Enter your First Number : "))
b = int(input("Enter your Second Number : "))
operation = input("Choose +,-,/,x : ")

if operation == "+":
    print("Result : ", a+b)
elif operation == "-":
    print("Result : ", a-b)
elif operation == "/":
    print("Result : ", a/b)
elif operation == "x":
    print("Result : ", a*b)
else :
    print("Invalid Operation")

text = input("Enter your Name")
print("Your Reversed Name : " , text[::-1])