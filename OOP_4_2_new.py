# Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание, умножение,
# деление и возведение в степень. Программа должна выдавать сообщения об ошибке и продолжать работу при вводе
# некорректных данных, делении на ноль и возведении нуля в отрицательную степень.

def addition(a, b):
    return a+b


def subtraction(a, b):
    return a-b


def multiplication(a, b):
    return a*b


def division(a, b):
    return a/b


def exponent(a, b):
    return a**b


while True:
    try:
        var_1 = int(input("Enter first number: "))
        result = var_1
        break
    except ValueError:
        print("Error. Enter only numbers.")


def input_operation():
    operation_symb = ["+", "-", "*", "/", "**"]
    while True:
        try:
            operation = input("Enter operation +, -, *, /, ** : ")
            if operation in operation_symb:
                return operation
            else:
                print("Wrong operation.")
        except ValueError:
            print("Value error")


operation = input_operation()


while True:
    try:
        var_2 = int(input("Enter second number: "))
        break
    except ValueError:
        print("Error. Enter only numbers.")


result = var_1
if operation != "=":
    if operation == "+":
        result = addition(result, var_2)
        print(result)
    elif operation == "-":
        result = subtraction(result, var_2)
        print(result)
    elif operation == "*":
        result = multiplication(result, var_2)
        print(result)
    elif operation == "/":
        try:
            result = division(result, var_2)
            print(result)
        except ZeroDivisionError as error:
            print("You csant divide by zero", error)
    elif operation == "**":
        try:
            result = exponent(result, var_2)
            print(result)
        except ZeroDivisionError as error:
            print("Enter value greater then zero", error)
else:
    print(result)
