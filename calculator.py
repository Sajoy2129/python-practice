# A simple menu-based calculator that runs in the terminal.

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: can't divide by zero"
    return a / b


def power(a, b):
    # A negative number to a fractional power (like -8 ** 0.5) has no real answer.
    if a < 0 and b != int(b):
        return "Error: can't raise a negative number to a fractional power"
    try:
        return a ** b
    except OverflowError:
        return "Error: result is too large"
    except ZeroDivisionError:
        return "Error: can't raise 0 to a negative power"


def square_root(a):
    if a < 0:
        return "Error: can't take the square root of a negative number"
    return math.sqrt(a)


def quit_program():
    print("Goodbye!")


def show_menu():
    print()
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square root")
    print("7. Quit")


def get_number(prompt):
    while True:
        text = input(prompt)
        try:
            number = float(text)
        except ValueError:
            print("Please enter a number.")
            continue

        # float() also accepts "inf" (infinity) and "nan" (not a number), so reject those.
        if not math.isfinite(number):
            print("Please enter a regular number.")
            continue

        return number


def main():
    print("Simple Calculator")

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ")

        if choice == "7":
            quit_program()
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice, please pick 1-7.")
            continue

        # Square root only needs one number.
        if choice == "6":
            a = get_number("Number: ")
            print("Result:", square_root(a))
            continue

        a = get_number("First number: ")
        b = get_number("Second number: ")

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
        else:
            result = power(a, b)

        print("Result:", result)


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        # Input ended (Ctrl+D, or no keyboard available), so exit politely.
        print()
        quit_program()
