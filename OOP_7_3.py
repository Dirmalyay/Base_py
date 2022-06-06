# Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова данного текста.

my_str = input("Enter some text: ")
my_str_lower = my_str.lower()
words = my_str_lower.split()
sort_ = words.sort()

print(words)
