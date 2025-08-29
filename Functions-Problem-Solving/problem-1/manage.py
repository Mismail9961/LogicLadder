# Nested dictionary for student records
students = {
    "101": {
        "name": "Ali",
        "age": 20,
        "grade": "A",
        "subjects": {
            "Math": 95,
            "English": 88,
            "Science": 92
        }
    },
    "102": {
        "name": "Sara",
        "age": 19,
        "grade": "B+",
        "subjects": {
            "Math": 85,
            "English": 90,
            "Science": 78
        }
    },
    "103": {
        "name": "Omar",
        "age": 21,
        "grade": "A-",
        "subjects": {
            "Math": 89,
            "English": 76,
            "Science": 91
        }
    }
}


for student_id in students:
    print("\nStudent ID:", student_id)
    print("Name:", students[student_id]["name"])
    print("Age:", students[student_id]["age"])
    print("Grade:", students[student_id]["grade"])

    for subject in students[student_id]['subjects']:
        print("  ", subject, ":", students[student_id]["subjects"][subject])
    