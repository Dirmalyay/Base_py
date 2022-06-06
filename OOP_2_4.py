# Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех транспортных
# средств поля, в наследниках – специфичные для них. Создайте несколько экземпляров.
# Выведите информацию о каждом транспортном средстве.

class Transport:
    def __init__(self, price, color, speed, model, marc):
        self.price = price
        self.color = color
        self.speed = speed
        self.model = model
        self.marc = marc

    def __str__(self):
        return f'{self.price}, {self.color}, {self.speed}, {self.model}, {self.marc}'

    def action(self):
        print("I can move.")

    def print_info(self):
        print(f'{self.price}, {self.color}, {self.speed}, {self.model}, {self.marc}')


class Bicycl(Transport):
    def __init__(self, price, color, speed, model, marc, type1):
        super().__init__(price, color, speed, model, marc)
        self.type1 = type1

    def type_of_using(self):
        print(f"Transport could be for the mountains or for the city. It depends from type: {self.type1}")
        return self.print_info()


class Car(Transport):
    def __init__(self, price, color, speed, model, marc, engine):
        super().__init__(price, color, speed, model, marc)
        self.engine = engine

    def engine_power(self):
        print(f"Engine could be electric or use gasoline: {self.engine}")
        super().print_info()


bicycl1 = Bicycl(100, "red", 60, "hhjk7", "author", "mount")
bicycl1.type_of_using()
print()
car1 = Car(1000, "black", 200, "NS100", "mercedes", "gasoline")
car1.engine_power()
