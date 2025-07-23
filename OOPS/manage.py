# class Person:
#     pass

# p1 = Person()  

# class PersonData:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 

#     def __str__(self):
#         return f"Name:{self.name} and Age:{self.age}"

# obj = PersonData("ismail",18)
# print(obj)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def display(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
    
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display(self):
        super().display()
        print(f"Grade : {self.grade}")

class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary

    def display(self):
        super().display()
        print(f"Salary: {self.salary}")

# Create Student object
s1 = Student("Ismail", 20, "A" , 10000)

# Call display method
s1.display()
