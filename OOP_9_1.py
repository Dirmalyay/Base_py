# Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных действительных чисел.
# Создайте ещё один скрипт, который читает числа из файла и выводит на экран их сумму.
import random

def create_rand():
    rand_num = []
    for i in range(0, 1000):
        rand_num.append(random.randint(0, 1000))
    with open("rand_num.txt", "w") as rn:
        for i in rand_num:
            rn.write(str(i)+'\n')


def sum_rand():
    with open("rand_num.txt", "r") as rn:
        res = sum(map(int, rn))
    print(res)


create_rand()
sum_rand()
