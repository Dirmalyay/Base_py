# Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть реализована возможность
# ввода изначальной ссылки и короткого названия и получения изначальной ссылки по её названию.

link_1 = input("Enter the link: ")
short_link_1 = input("Enter short name: ")
links_dict = dict()
links_dict[short_link_1] = link_1
print(links_dict)
a = input("Enter short name to get full link: ")
for link_1 in links_dict:
    if link_1 == a:
        print(links_dict[link_1])
    else:
        print("Wrong short name.")
