def count_digits(num):
    num = abs(num)
    return len(str(num))

n = 12345
print("Number of digits:", count_digits(n))