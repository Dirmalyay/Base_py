# Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом,
# чтобы у него была основная часть, которая отвечала бы за логику работы и предоставляла обобщённый интерфейс,
# и модуль представления, который отвечал бы за взаимодействие с пользователем. При замене последнего на другой,
# взаимодействующий с пользователем иным способом, программа должна продолжать корректно работать.
import OOP_9_2

while True:
    print("1. - Add link\n"
          "2. - Read link\n"
          "3. - Exit")

    var = input("Enter the number of operation: ")
    if var == "1":
        OOP_9_2.write_link()
    elif var == "2":
        OOP_9_2.read_link()
    elif var == "3":
        break
    else:
        print("Wrong operator.")
