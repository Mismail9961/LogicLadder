num = int(input("Enter A Number"))

fractional = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1,num+1):
        fractional *= i
    print(f"Factorial of {num} is {fractional}")
