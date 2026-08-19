# Simple Calculator
# Author: Your Name

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error: Cannot calculate modulus with zero."
    return a % b


def power(a, b):
    return a ** b


while True:

    print("\n==============================")
    print("       PYTHON CALCULATOR")
    print("==============================")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "7":
        print("\nThank you for using the calculator!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("\nInvalid choice. Please select 1-7.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)

        elif choice == "2":
            result = subtract(num1, num2)

        elif choice == "3":
            result = multiply(num1, num2)

        elif choice == "4":
            result = divide(num1, num2)

        elif choice == "5":
            result = modulus(num1, num2)

        elif choice == "6":
            result = power(num1, num2)

        print("\nResult:", result)

    except ValueError:
        print("\nError: Please enter valid numbers.")