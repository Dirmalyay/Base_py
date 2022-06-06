class Animal:
    def animal_disc_1(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        print(f"This is {self.name}. He is {self.age} yers old. His color is {self.color}.")


mouse = Animal()
dog = Animal()
duck = Animal()
mouse.animal_disc_1("Miky", 70, "gray")
dog.animal_disc_1("Guffy", 62, "yellow")
duck.animal_disc_1("Skruge", 90, "white")
