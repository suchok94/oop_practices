# task № 2
class Book:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    def open_book(self, pages):
        if self.pages < pages:
            print(f'Книга {self.name} не может быть открыта на {pages} странице!')
        else:
            print(f'Книга {self.name} открыта на странице номер {pages}!')

    def info_about_book(self):
        print(f'Информация о книге:\nНаименование: {self.name}\nАвтор: {self.author}\nКоличество страниц: {self.pages}')

class Program:
    @staticmethod
    def main():
        pass

Program.main()