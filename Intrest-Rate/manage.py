def intrest_rate():
    print("Welcome to the intrest rate calculator")
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of intrest: "))
    time = float(input("Enter the time in years: "))
    intrest = (principal * rate * time) / 100
    print(f"The intrest is {intrest}")

intrest_rate()