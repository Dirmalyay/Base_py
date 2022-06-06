# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов.
# Сделайте так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.
class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre


class Review(Book):
    def __init__(self, author, title, year, genre, _rew):
        self.rew = _rew
        Book.__init__(self, author, title, year, genre)

    def dscription(self, rew):
        self.rew.append(rew)
        return self.rew

    def __str__(self):
        return f"Info: {self.author, self.title, self.year, self.genre, self.rew}"


book_1 = Review("Манн", "Будденброки", 1901, "roman", [])
book_1.dscription("Good book")
book_1.dscription("Bad book")
print(book_1.__str__())
