# Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год поступления на работу.
# Конструктор должен генерировать исключение, если заданы неправильные данные. Введите список работников с клавиатуры.
# Выведите всех сотрудников, которые были приняты после заданного года.

class Worker:
    def __init__(self, name, second_name, department, year_of_admission):
        if type(name) == str:
            if str(name)[0].isupper():
                self. name = name
            else:
                raise ValueError('Name should start from upper letter')
        else:
            raise ValueError('First name cannot contain any digits')
        if type(second_name) == str:
            if str(second_name)[0].isupper():
                self.second_name = second_name
            else:
                raise ValueError('Name should start from upper letter')
        else:
            raise ValueError('Second name cannot contain any digits')

        self.department = department

        if type(year_of_admission) == int:
            self.year_of_admission = year_of_admission
        else:
            raise TypeError('Enter integer number.')

        self.info = [self.name, self.second_name, self.department, self.year_of_admission]

    def __str__(self):
        return print(f'{ self. name}, {self.second_name}, {self.department} {self.year_of_admission}')


if __name__ == '__main__':
    worker_list = []
    n = int(input("Enter number of workers: "))
    y = int(input("Enter the year for demj info: "))

    for i in range(0, n):
        name = input("Enter the name: ")
        second_name = input("Enter the second name: ")
        department = input("Enter the department: ")
        year_of_admission = int(input("Entre the year of admission: "))
        worker = Worker(name, second_name, department, year_of_admission)
        worker_list.append(worker)
        if worker.year_of_admission > y:
            print(worker.info)
        else:
            print("You can't work from this year.")
