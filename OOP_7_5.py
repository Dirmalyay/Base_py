# Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит её отсортированной
# в порядке возрастания.

text_for_sort = input("Enter numbers for sorting: ")
num_list = []
for i in text_for_sort.split():
    try:
        if type(i) == float(i) or int(i):
            num_list.append(i)
            num_list.sort()
    except ValueError:
        print(ValueError)
print(num_list)
