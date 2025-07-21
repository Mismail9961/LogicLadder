import random
# for i in range(5):
#     print("Hello", i)

# count = 0 
# while count < 5 :
#     print("Counting" , count)
#     count += 1

# range(5)         # 0 to 4
# range(1, 6)      # 1 to 5
# range(0, 10, 2)  # 0, 2, 4, 6, 8

# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])        # apple
# print(fruits[-1])       # cherry

# for fruit in fruits :
#     print("I Like ", fruit)

# fruits.append("mango")   # Add item
# fruits.sort()            # Sort items
# print(len(fruits))       # Length of list

# num2 = [1, 3, 5, 7, 9, 2, 4, 6, 8]
# num2.sort()
# print(num2)

# num = [1,3,5,7,9,2,4,6,8]
# print(sorted(num))



number = random.randint(1,10)
attempts = 0 

print("Guess the number between 1 and 10!")

while True :
    guess = int(input("Enter your Number"))
    attempts += 1

    if guess < number :
        print("To Low")
    elif guess > number :
        print("To High")
    else :
        print(f"Correct! You guessed it in {attempts} attempts.")
        break