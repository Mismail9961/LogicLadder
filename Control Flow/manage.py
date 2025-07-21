age = int(input("Enter your Age"))
if age >= 18:
    print("You are an Adult")
elif age >= 13:
    print("You are a teenager")
else :
    print("You are a child ")


# and = both conditions must be true
if age > 13 and age < 19:
    print("Teen")

# or = at least one must be true
if age < 13 or age > 60:
    print("Child or Senior")

# not = reverses condition
is_day = True
if not is_day:
    print("It's night.")


admin_email = input("Enter your Email")
admin_password = input("Enter your Password")

admin_stored_email = "ismail@gmail.com"
admin_stored_password = "tt6789"

if admin_email == admin_stored_email :
    if admin_password == admin_stored_password:
        print("Welcome Back")
    else:
        print("Wrong Password or Email")
else : 
    print("Invalid User")


#BMI Formula :
weight = float(input("Enter your Weight (kg) : "))
height = float(input("Enter your Height (m) : "))

bmi = weight / (height ** 2)

print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")



score = 0

print("Welcome to python Quiz!")

q1 = input("1. What is the output of 2 ** 3? ")
if q1 == "8":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

q2 = input("2. Which keyword is used for functions in Python? ")
if q2 == "def":
    score += 1
    print("Correct!")
else:
    print("Wrong!")


print(f"\nYour total score is: {score}")