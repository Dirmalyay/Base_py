# Создайте модуль для получения простых чисел. Импортируйте его из другого модуля. Импортируйте отдельные его имена.

import OOP_10_3_mod1
from OOP_10_3_mod1 import simp_num


def req_num():
    try:
        request = int(input("Enter the number to which you want to display sequence: "))
        print(simp_num(request))
    except ValueError:
        print("Enter integer number.")


if __name__ == "__main__":
    req_num()
