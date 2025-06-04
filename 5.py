class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_info(self):
        return f"Ім'я: {self.name}, Рік народження: {self.birth_year}"


class Book:
    def __init__(self, title, author, year, annotation=""):
        self.title = title
        self.author = author  # агрегація: автор існує незалежно
        self.year = year
        self.annotation = annotation

    def get_info(self):
        info = f"Назва: {self.title}, Рік видання: {self.year}, Автор: {self.author.name}"
        if self.annotation:
            info += f"\nАнотація: {self.annotation}"
        return info


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книгу '{book.title}' додано до бібліотеки '{self.name}'.")

    def list_books(self):
        if not self.books:
            return "У бібліотеці немає книг."
        return "\n\n".join(book.get_info() for book in self.books)

    def find_books_by_author(self, author_name):
        found = [book for book in self.books if book.author.name.lower() == author_name.lower()]
        if not found:
            return f"Книг автора '{author_name}' не знайдено."
        return "\n\n".join(book.get_info() for book in found)


def menu():
    print("=== Бібліотечна система ===")
    library_name = input("Введіть назву бібліотеки: ")
    library = Library(library_name)
    authors = []

    while True:
        print("\n--- Меню ---")
        print("1. Додати автора")
        print("2. Додати книгу")
        print("3. Переглянути всі книги")
        print("4. Знайти книги за автором")
        print("5. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            name = input("Ім'я автора: ")
            year = input("Рік народження: ")
            authors.append(Author(name, year))
            print(f"Автор {name} доданий.")

        elif choice == "2":
            if not authors:
                print("Спочатку додайте хоча б одного автора.")
                continue
            print("Оберіть автора:")
            for idx, a in enumerate(authors):
                print(f"{idx + 1}. {a.get_info()}")
            try:
                author_index = int(input("Номер автора: ")) - 1
                if author_index not in range(len(authors)):
                    print("Неправильний номер.")
                    continue
            except ValueError:
                print("Введіть число.")
                continue

            title = input("Назва книги: ")
            year = input("Рік видання: ")
            annotation = input("Анотація (необов'язково): ")
            book = Book(title, authors[author_index], year, annotation)
            library.add_book(book)

        elif choice == "3":
            print("\n=== Список книг у бібліотеці ===")
            print(library.list_books())

        elif choice == "4":
            name = input("Введіть ім'я автора: ")
            print("\n=== Результати пошуку ===")
            print(library.find_books_by_author(name))

        elif choice == "5":
            print("Завершення програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    menu()
