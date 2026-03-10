class Book:
    def __init__(self, name, author, count=1):
        self.name = name
        self.author = author
        self.count = count

    def __str__(self):
        return f"Книга: {self.name} | Автор: {self.author} | Кількість: {self.count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name, author):
        for book in self.books:
            if book.name == name and book.author == author:
                book.count += 1
                return
        self.books.append(Book(name, author))

    def user_take_book(self, name, author):
        for book in self.books:
            if book.name == name and book.author == author:
                if book.count > 0:
                    book.count -= 1
                    print("Книгу видано")
                else:
                    print("Книги немає в наявності")
                return
        print("Такої книги не існує")

    def show_books(self):
        for book in self.books:
            print(book)


library = Library()

library.add_book("Harry Potter", "J.K. Rowling")
library.add_book("Harry Potter", "J.K. Rowling")
library.add_book("1984", "George Orwell")
library.add_book("Воно", "Stephen King")
library.add_book("Мертва зона", "Stephen King")

library.show_books()

library.user_take_book("Harry Potter", "J.K. Rowling")
library.show_books()