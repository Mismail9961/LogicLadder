# # Dictionaries (Key-Value Pairs)
# person = {"name":"Ismail" , "age":18}

# #Create/Add
# person["city"] = "Lahore"
# print(person)

# #Read
# print(person["name"])

# #update
# person["age"] = 20

# #Delete 
# del person["city"]
# print(person)


# numbers = {1, 2, 3, 4}

# # Add
# numbers.add(5)

# # Remove
# numbers.remove(2)

# # Operations
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.union(b))       # {1, 2, 3, 4, 5}
# print(a.intersection(b))# {3}



# coordinates = (10, 20)

# # Accessing
# print(coordinates[0])  # 10

# # Tuples are immutable
# # coordinates[0] = 5  ❌ This will raise an error


# def word_frequency(text):
#     words = text.split()
#     frequency = {}

#     for word in words:
#         word = word.lower()
#         frequency[word] = frequency.get(word,0) + 1

#     return frequency


# sentence = "Python is great and Python is easy"
# print(word_frequency(sentence))

#Mini Project
students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter your Name: ")
    grade = input("Enter your Grade: ")
    
    students[roll] = {"name": name, "grade": grade}
    print("Student Added Successfully.")

def view_students():
    if len(students) == 0:
        print("No records found.")
    else:
        for roll in students:
            print(f"Roll: {roll}, Name: {students[roll]['name']}, Grade: {students[roll]['grade']}")

def update_student():
    roll = input("Enter Roll Number to Update")
    if roll in students:
        name =  input("Enter New Name : ")
        grade = input("Enter New Grade : ")
        students[roll] = {"name": name, "grade": grade}
        print("Student updated.")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to Delete the student : ")
    if roll in students :
        del students[roll]
        print("Student Deleted.")
    else : 
        print("Student Not Found.")


def main():
    while True:
        print("\n--- Student Record System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

main()
