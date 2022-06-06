# Создайте 2 класса – языка, например, английский и испанский. У обоих классов должен быть метод greeting().
# Оба создают разные приветствия. Создайте два соответствующих объекта из двух классов выше и вызовите действия
# этих двух объектов в одной функции (функция hello_friend).

class English:
    def greeting(self):
        return f"Good afternoon"


class Spanish:
    def greeting(self):
        return f"Buena tarde"


def hello_friend(eng, span):
    print("Hello friend!", eng)
    print("Hola!", span)


en = English()
sp = Spanish()
e = en.greeting()
s = sp.greeting()

hello_friend(e, s)
