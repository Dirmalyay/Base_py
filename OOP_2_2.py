# Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать нажатия мыши.
# Опишите класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите метод нажатия на кнопку.

# from tkinter import *
from turtle import *


class GraphicObj:
    obj = Turtle()

    def __init__(self, shape_, color_):
        self.shape_ = shape_
        self.color_ = color_

    def create_obj(self):
        self.obj.shape(self.shape_)
        self.obj.color(self.color_)
        # exitonclick()


'''class Rectangle:
    rect = Tk()
    canvas = Canvas(rect, height=500, width=600, bg='#133')
    canvas.pack()

    def __init__(self, h1, h2, w1, w2):
        self.h1 = h1
        self.h2 = h2
        self.w1 = w1
        self.w2 = w2

    def create_rect(self):
        self.canvas.create_rectangle(self.h1, self.h2, self.w1, self.w2, fill='red')
        self.rect.mainloop()
        exitonclick()'''


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def create_rect(self):
        for i in range(0, self.a):
            for j in range(0, self.b):
                print("* ", end="")
            print()


class MousePress:

    def __init__(self):
        pass

    def press_action(self):
        print("button press response")


class Button(Rectangle, MousePress):

    def __init__(self, a, b):
        super().__init__(a, b)

    def press_button(self):
        super().create_rect()
        super().press_action()
        print("button pressed")

obj_1 = GraphicObj('circle', 'green')
obj_1.create_obj()

rect_1 = Rectangle(5, 10)
butt_1 = Button(5, 10)

butt_1.press_button()
