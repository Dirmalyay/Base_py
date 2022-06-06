# Реализуйте цикл, который будет перебирать все значения итерабельного объекта iterable

class IterObj:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.var = self.start - self.step


    def __iter__(self):
        return self

    def __next__(self):
        if self.var + self.step < self.stop:
            self.var += self.step
            return self.var
        else:
            raise StopIteration


itarable = IterObj(1, 5, 1)
for i in itarable:
    print(i)
