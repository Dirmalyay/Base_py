# Создайте класс, описывающий отзыв к книге.
# Добавьте в класс книги поле – список отзывов.
# Сделайте так, что при выводе книги на экран
# при помощи функции print также будут выводиться отзывы к ней.
class Review:
    rew_list = list()

    def __init__(self):
        pass

    def __str__(self):
        return f"reviews: {self.rew_list}"

    def rew_create(self, rew):
        self.rew_list.append(rew)
        return self.rew_list


class Book:

    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.info = [author, title, year, genre]

    def __str__(self):
        return f"Book: {self.info}"

    def __repr__(self):
        return f"Book('{self.info}')"

    @staticmethod
    def connect_rew():
        return Review()

    def rew_add(self, text):
        self.object_rew = self.connect_rew()
        self.object_rew.rew_create(text)
        return self.object_rew


book_1 = Book("Luwis Carroll", "Alice in Wonderland", 1865, "tale")
print(book_1.info)
book_1.rew_add("Good")
book_1.rew_add("Bad")
print(book_1.rew_add("Neutral"))
