# Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed).

class ReverList:
    def __init__(self, list_for_revers):
        self.list_for_revers = list_for_revers
        # количество элементов
        self.element = len(self.list_for_revers) - 1
        # переменная для перебора
        self.var = self.element

    def __iter__(self):
        return self

    def __str__(self):
        return f'{self.var}'

    def __next__(self):
        if self.element < 0:
            raise StopIteration
        else:
            self.var = self.list_for_revers[self.element]
            self.element -= 1
            return self.var

if __name__ == '__main__':
    a = [2, 3, 4, 5, 7]
    b = ReverList(a)
    for i in b:
        print(b)



