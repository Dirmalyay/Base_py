operations = {
    "-": lambda a, b: a-b,
    "*": lambda a, b: a*b,
    "/": lambda a, b: a/b,
    "**": lambda a, b: a**b,
    "+": lambda a, b: a+b,
}

while True:
    try:
        c = input("Enter operation + - * / **: (for exit print - s) ")
        if c != "s":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(operations[c](a, b))
        else:
            break
    except ZeroDivisionError:
        print("You can't divide by zero.")
