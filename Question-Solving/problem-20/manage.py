num = int(input("Enter a number: "))

digit_sum = sum(int(d) for d in str(abs(num)))
print(f"The sum of digits of {num} is {digit_sum}")
