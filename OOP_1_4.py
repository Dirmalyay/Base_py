# Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список автомобилей,
# доступных для продажи, и функцию продажи заданного автомобиля.

class Car:
    def __init__(self, index, color, brand, price, _elem):
        self.index = index
        self.color = color
        self.price = price
        self.brand = brand
        self.elem = _elem

    # def __str__(self):
        # return f"Info: {self.index, self.color, self.brand, self.price, self.elem}"

    def car_element(self):
        self.elem.extend([self.index, self.color, self.brand, self.price])
        return self.elem


class Salon(Car):
    def __init__(self, index, color, brand, price, _elem, _total_quantity):
        self.total_quantity = _total_quantity
        Car.__init__(self, index, color, brand, price, _elem)

    def salon_list(self, _elem):
        self.total_quantity.append(self.elem)
        return self.total_quantity

    def sell_car(self, _elem):
        for i in self.total_quantity:
            if i == self.elem:
                del(self.elem)
                return self.total_quantity


car_1 = Salon(111, "Red", "BMW", 20000, [], [])
car_2 = Salon(222, "Blue", "BMW", 30000, [],[])

print(car_1.car_element())
print(car_2.car_element())

print(car_1.salon_list(car_2))
print(car_1.salon_list(car_2))
