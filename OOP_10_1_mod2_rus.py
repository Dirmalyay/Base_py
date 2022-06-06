import OOP_9_2

while True:
    print("1. - Добавить короткое имя ссылке.\n"
          "2. - Вернуть по короткому имени.\n"
          "3. - Выход")

    var = input("Введите номер операции: ")
    if var == "1":
        OOP_9_2.write_link()
    elif var == "2":
        OOP_9_2.read_link()
    elif var == "3":
        break
    else:
        print("Номер операции указан неверно.")
