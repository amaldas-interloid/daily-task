def add():
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    print("sum",a + b)
def substract():
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    print("difference",a - b)
def greet():
    name = input("Enter your name: ")
    print("Hello", name)
# def exit_program():
#     print("Exiting program...")
#     exit()
while True:
    print("1===== .......MENU......... =====")
    print("1. Add Numbers")
    print("2. Subtract Numbers")
    print("3. Greeting")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add()
    elif choice == "2":
        substract()
    elif choice == "3":
        greet()
    elif choice == "4":
        # exit_program()
        print("exiting program........")
        break
    else:
        print("invalid choice")

    
