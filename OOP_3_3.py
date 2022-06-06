# Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
# Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и позволяющий задавать
# и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут быть заданы в одной шкале,
# а получены в другой.

class Temperature:
    def __init__(self):
        self.__data = 0

    @property
    def data(self):
        return self.__data

    # @data.getter
    def data(self):
        while True:
            self.data = int(input("Enter value: "))
            a = input("To convert from Celsius to Fahrenheit, press F.\n "
                      "To convert from Fahrenheit to Celsius, press C: ")
            if a == "F":
                self.fahrenheit()
            elif a == "C":
                self.celsius()
            else:
                print("Wrong value. Try again.")

    def celsius(self):
        cel = (self.__data - 32) / 1.8
        print(cel)

    def fahrenheit(self):
        far = self.__data * 1.8 + 32
        print(far)

temp1 = Temperature()
temp1.data()
