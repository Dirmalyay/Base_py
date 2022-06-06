# Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список автомобилей,
# доступных для продажи, и функцию продажи заданного автомобиля.
class Car:
    def __init__(self, color, model, price):
        self.color = color
        self.model = model
        self.price = price
        self.car_info = [color, model, price]

    def __str__(self):
        return f"{self.car_info}"

    def __repr__(self):
        return f"{self.car_info}"


class Salon:
    car_list = list()

    def __init__(self):
        pass

    def __str__(self):
        return f"{self.car_list}"

    def car_create(self, element):
        self.car_list.append(element)
        return self.car_list

    def remove_car(self, sold_elem):
        self.car_list.remove(sold_elem)
        return self.car_list

    @staticmethod
    def create_obj_car():
        return Car

    def add_car(self, element):
        self.car_elem = self.create_obj_car()
        self.car_elem = self.car_create(element)
        return self.car_elem


car_1 = Car("red", "BMW", 30000)
car_2 = Car("blue", "BMW", 40000)
car_3 = Car("black", "BMW", 60000)
salon = Salon()
salon.add_car(car_1)
salon.add_car(car_2)
salon.add_car(car_3)
print(salon)

salon.remove_car(car_2)
print(salon)
