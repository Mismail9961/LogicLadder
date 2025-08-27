from collections import Counter

numbers = [1, 2, 2, 3, 1, 4, 2, 5, 3, 3]
frequency = Counter(numbers)

print(frequency)
# Output: Counter({2: 3, 3: 3, 1: 2, 4: 1, 5: 1})
