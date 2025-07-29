# Simple To-Do List App (Console Version)

todo_list = []

def show_menu():
    print("\n==== To-Do List ====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def show_tasks():
    if not todo_list:
        print("📝 No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    todo_list.append(task)
    print("✅ Task added.")

def remove_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to remove: "))
        removed = todo_list.pop(task_no - 1)
        print(f"❌ Task '{removed}' removed.")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please select 1-4.")
