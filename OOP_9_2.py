# Модифицируйте исходный код сервиса по сокращению ссылок из предыдущих двух уроков так, чтобы он сохранял базу
# ссылок на диске и не «забывал» при перезапуске. При желании можете ознакомиться с модулем shelve
# (https://docs.python.org/3/library/shelve.html), который в данном случае будет весьма удобен и
# упростит выполнение задания.
import shelve


def write_link():
    link_1 = input("Enter the link: ")
    storage = shelve.open("links.txt")
    short_link_1 = input("Enter short name: ")
    storage[short_link_1] = link_1
    storage.close()


def read_link():
        name_get = input("Enter short name to get full link: ")
        storage = shelve.open("links.txt")
        try:
            long_link_get = storage[name_get]
            print("Full link: ", long_link_get)
        except KeyError:
            print("This name does not exist.")

