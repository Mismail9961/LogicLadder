HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            history = file.readlines()
    except FileNotFoundError:
        print("No history file found.")
        return

    if not history:
        print("No history found.")
    else:
        for line in reversed(history):
            print(line.strip())

def clear_history():
    with open(HISTORY_FILE, "w"):
        pass
    print("History cleared.")

def save_history(equation, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Please enter an equation in the format 'number operator number'.")
        return

    try:
        num1 = float(parts[0])
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers. Please enter valid numeric values.")
        return

    operator = parts[1]

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return

    if result.is_integer():
        result = int(result)

    print(f"{user_input} = {result}")
    save_history(user_input, result)

def main():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Show History")
        print("2. Clear History")
        print("3. Calculate")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_history()
        elif choice == "2":
            clear_history()
        elif choice == "3":
            user_input = input("Enter an equation: ")
            calculate(user_input)
        elif choice == "4":
            print("Thank you for using the Simple Calculator!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
