class Animal:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def print_info(self):
        return f"{self.name, self.age, self.color}"


class Dog(Animal):

    def voice(self):
        super().print_info()
        print("Gav-gav")


class Cat(Animal):
    def voice(self):
        super().print_info()
        print("Mew-mew")


pussy = Cat("Vasya", 5, "black")
print(pussy.print_info())
pussy.voice()
