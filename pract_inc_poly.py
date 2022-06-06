class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    @staticmethod
    def __print_info():
        print("i'm a car.")

    def call_print_info(self):
        self.__print_info()


class UpdateCar(Car):

    def __init__(self, model, color, year, price):
        super().__init__(model, color, year)
        self._price = price

    def __print_info(self):
        return f'{self.model} {self.color} {self.color} {self._price}'

    def get_price(self):
        return self.__print_info()

    def _set_price(self):
        print("Do you want to change the price?")
        self.value = input('Enter Y or N: ')
        if self.value == "Y":
            value2 = input("Enter new price: ")
            self._price = value2
            print(f'{self._price}')
        else:
            print("Buy")


car1 = UpdateCar("BMW", "Green", 1986, 2000)
car1.get_price()
car1._set_price()
