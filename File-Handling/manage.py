#Write in File
with open("sample.txt","w") as file :
    file.write("Hello World!")

#Read File 
with open("sample.txt","r") as file : 
    content = file.read()
    print(content)

# Error Handling
try:
    number = int(input("Enter a Number"))
    print(10/number)
except ZeroDivisionError:
    print("Cannot Divide By zero")
except ValueError:
    print("Invalid Input, Please Enter a Number")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.read().splitlines()
    except:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        file.write("\n".join(tasks))

def show_tasks(tasks):
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")
    except:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. Show Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

main()
