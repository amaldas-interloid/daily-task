def add():
    count = int(input("How many numbers do you want to add: "))
    total = 0
    for i in range(count):
        num = int(input(f"Enter number {i + 1} : "))
        total += num
    print("Sum =", total)
def subtract():
    count = int(input("How many numbers do you want to subtract: "))
    first = int(input("Enter number 1: "))
    result = first
    for i in range(1, count):
        num = int(input(f"Enter number {i + 1}: "))
        result -= num
    print("Difference =", result)
def greet():
    name = input("Enter your name: ")
    print("Hello", name)
while True:
    print("\n===== MENU =====")
    print("1. Add Numbers")
    print("2. Subtract Numbers")
    print("3. Greeting")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add()
    elif choice == "2":
        subtract()
    elif choice == "3":
        greet()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")