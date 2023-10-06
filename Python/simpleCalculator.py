<<<<<<< HEAD
# Program make a simple calculator


# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
=======
# Define functions for the operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

>>>>>>> 0eaf03475a171f486a61ec62439dada704ba20b6
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Display the menu and get user input
while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Calculator is exiting. Goodbye!")
        break

<<<<<<< HEAD
    # check if choice is one of the four options
    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
=======
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")
>>>>>>> 0eaf03475a171f486a61ec62439dada704ba20b6

    else:
        print("Invalid Input")

