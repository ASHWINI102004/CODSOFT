# Express a function for each operation
def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        return "Error: Division by the zero is not allowed"

# Main program
def calculator():
    print("Simple Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get out the inputs of operation choice
    choice = input("Enter the choice (1,2,3,4): ")

    # Get out the inputs of two numbers
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    # Performs all the calculation based on user's choice
    if choice == '1':
        print(f"{number1} + {number2} = {add(number1, number2)}")
    elif choice == '2':
        print(f"{number1} - {number2} = {subtract(number1, number2)}")
    elif choice == '3':
        print(f"{number1} * {number2} = {multiply(number1, number2)}")
    elif choice == '4':
        print(f"{number1} / {number2} = {divide(number1, number2)}")
    else:
        print("Invalid choice")

# Run the calculator program
calculator()