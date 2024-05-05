# task № 2
class Book:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    def open_book(self, pages):
        if self.pages < pages:
            print('Книга не может быть открыта на этой странице!')
        else:
            print(f'Книга открыта на странице номер {pages}!')

    def info_about_book(self):
        print(f'Информация о книге:\n Наименование: {self.name}\nАвтор: {self.author}\nКоличество страниц: {self.pages}')
