# Bookクラスを定義します。このクラスは各本を表現します。
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        if self.is_checked_out:
            return False
        else:
            self.is_checked_out = True
            return True

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        else:
            return False

# Libraryクラスを定義します。このクラスは図書館を表現します。
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book.check_out():
                return True
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.return_book():
                return True
        return False
