# Create a dictionary
student = {
    "name": "Ali",
    "age": 21,
    "grade": "A",
    "city": "Karachi"
}

# Iterate over keys
print("Keys:")
for key in student:
    print(key)

# Iterate over values
print("\nValues:")
for value in student.values():
    print(value)

# Iterate over key-value pairs
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(f"{key}: {value}")
