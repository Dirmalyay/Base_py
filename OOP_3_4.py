# Опишите два класса Base и его наследника Child с методами method(),
# который выводит на консоль фразы соответственно "Hello from Base" и "Hello from Child".

class Base:
    def __init__(self):
        pass

    @staticmethod
    def method():
        print('Hello from Base.')


class Child(Base):
    def __init__(self):
        pass

    @staticmethod
    def method():
        print('Hello from Child.')


Base.method()

Child.method()
