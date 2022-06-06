# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
# если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.

class MyException(Exception):
    def __init__(self, var_1):
        self.var_1 = var_1


def check_value():
    try:
        var = input("Enter secret word: ")
        if var == "crazy":
            raise MyException("Forbidden word.")
    except MyException as me:
        print(me)
    else:
        print(var)


check_value()
