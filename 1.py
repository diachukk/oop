class Book:
    def __init__(self, title, author, year, pages, genre):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.genre = genre

    def get_info(self):
        return f"Назва: {self.title}, Автор: {self.author}, Рік видання: {self.year}, Сторінок: {self.pages}, Жанр: {self.genre}"

    def is_modern(self):
        return self.year > 2010

    def is_genre(self, genre_name):
        return self.genre.lower() == genre_name.lower()

    def compare_pages(self, other_book):
        if self.pages > other_book.pages:
            return f"Книга '{self.title}' має більше сторінок, ніж '{other_book.title}'."
        elif self.pages < other_book.pages:
            return f"Книга '{other_book.title}' має більше сторінок, ніж '{self.title}'."
        else:
            return f"Книги '{self.title}' та '{other_book.title}' мають однакову кількість сторінок."

book1 = Book("1984", "Джордж Орвелл", 1949, 328, "антиутопія")
book2 = Book("Дюна", "Френк Герберт", 1965, 412, "фантастика")
book3 = Book("Марсіанин", "Енді Вейр", 2011, 369, "фантастика")
book4 = Book("Тіні забутих предків", "Михайло Коцюбинський", 1911, 145, "роман")


#тест
print(book1.get_info())
print("Сучасна?" , book1.is_modern())
print(book3.get_info())
print("Сучасна?" , book3.is_modern())
print("Фантастика?" , book3.is_genre("Фантастика"))

print(book1.compare_pages(book2))

library = [book1, book2, book3, book4]

def find_book_by_title(title, library):
    for book in library:
        if book.title.lower() == title.lower():
            return book.get_info()
    return "Книгу не знайдено."


print(find_book_by_title("Дюна", library))
print(find_book_by_title("Гаррі Поттер", library))
