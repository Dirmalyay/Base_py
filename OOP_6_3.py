# Напишите функцию-генератор для получения n первых простых чисел.
def gen_simp_num(n):
    list_num = []
    for i in range(2, n+1):
        for j in list_num:
            if i % j == 0:
                break
        else:
            list_num.append(i)
    try:
        for k in list_num:
            yield k
    except StopIteration:
        print()


a = int(input("Enter num: "))
b = gen_simp_num(a)
while True:
    print(next(b))
