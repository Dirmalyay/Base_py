# Напишите генератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed).
def rev_list(list1):
    last_el_ind = len(list1) - 1
    while last_el_ind >= 0:
        element = list1[last_el_ind]
        last_el_ind = last_el_ind - 1
        yield element


list_for_rev = range(0, 10)
res = rev_list(list_for_rev)
n_l = []
for i in res:
    n_l.append(i)
print(n_l)