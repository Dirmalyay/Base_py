# Создать класс книга с атрибутами. Создайте несколько разных книг.
# Определите для него операции проверки на равенство и неравенство, методы __repr__ и __str__.
class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __eq__(self, other):
        return self.author == other.author, self.title == other.title, self.year == other.title,\
            self.genre == other.genre

    def __str__(self):
        return f"Info: {self.author, self.title, self.year, self.genre}"

    def __repr__(self):
        return f"Information { self.author, self.title, self.year, self.genre}"


book_1 = Book("Edgar Po", "Crow", 1845, "novelette")
book_2 = Book("Alexandr Pushkin", "Onegin", 1831, "poem")

print(book_1.__eq__(book_2))
print(book_1.__str__())
print(book_2.__repr__())
