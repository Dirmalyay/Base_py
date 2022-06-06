# Создайте иерархию классов с использованием множественного наследования. Выведите на экран порядок
# разрешения методов для каждого из классов. Объясните, почему линеаризации данных классов выглядят именно так.

class First:
    a = 1

    def __init__(self):
        print("First class")

    def description(self):
        print(f"If I specified first, then the child class will take my values and method: {self.a}")


class Second:
    b = 11

    def __init__(self):
        print("Second class")

    def description(self):
        print(f"If I specified first, then the child class will take my values and method: {self.b}")


class Third(Second, First):
    def __init__(self):
        print("Third class")


element = Third()
element.description()
