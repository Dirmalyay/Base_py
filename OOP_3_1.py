# Создайте класс, описывающий автомобиль. Какие атрибуты и методы должны быть полностью инкапсулированы?
# Доступ к таким атрибутам и изменение данных реализуйте через специальные методы (get, set).

class Car:
    def __init__(self, model, color, year, price):
        self.model = model
        self.color = color
        self.year = year
        self.__price = price
        self.__discount = self.__get_discount(price)

    def print_info(self):
        return f'Info: {self.model}, {self.color}, {self.year}'

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def __get_discount(self, __price):
        self.__price = self.__price*0.95
        return self.__price

    @property
    def discount(self):
        return self.__discount


car1 = Car("lexus", "black", 2022, 1000000)
print(car1.print_info())

car1.price = 20000
print(car1.discount)