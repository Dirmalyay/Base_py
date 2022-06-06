# Создайте модуль для получения простых чисел. Импортируйте его из другого модуля. Импортируйте отдельные его имена.

def simp_num(n):
   list_ = []
   for i in range(2, n+1):
       for j in list_:
           if i % j == 0:
               break
       else:
           list_.append(i)
   return list_
