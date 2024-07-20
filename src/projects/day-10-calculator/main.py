from art import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def exponent(a, b):
    return a ** b


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': exponent,
}


def calculator():
    num1 = float(input("What's the first number: "))
    for key in operations:
        print(key)

    while True:
        operation = input("Pick an operation: ")
        while operation not in operations:
            print("That's not a valid operation!")
            operation = input("Pick an operation: ")

        num2 = float(input("What's the other number?: "))

        result = operations[operation](num1, num2)

        print(f"{num1} {operation} {num2} = {result}")
        keep_going = input(f"\nType 'y' to continue calculating with {result}, 'n' to start a new calculation, "
                           f"or 'stop' to stop calculating: ")
        while keep_going not in ['y', 'n', 'stop']:
            print("That's not one of the choices.")
            keep_going = input(f"\nType 'y' to continue calculating with {result}, 'n' to start a new calculation, "
                               f"or 'stop' to stop calculating: ")

        if keep_going == "y":
            num1 = result
        elif keep_going == "n":
            calculator()
        else:
            return


print(logo)
calculator()