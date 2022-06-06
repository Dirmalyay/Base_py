# Выведите из списка чисел список квадратов четных чисел. Используйте 2 варианта решения: генератор и цикл
def gen():
    print("generator res: ")
    a = (x**2 for x in range(10) if x % 2 == 0 and x != 0)
    while True:
        try:
            print((next(a)), end=" ")
        except StopIteration:
            break


def sqr():
    print("cycle res: ")
    for i in range(10):
        if (i % 2 == 0 and i != 0):
            print(i**2, end=" ")


sqr()
print()
gen()
