from __future__ import annotations
# task 2
class Library:

    def __init__(self, name: str, address: str, books_list: list[Book] = None, employees_list: list[Employee] = None):
        self.__name = name
        self.__address = address

        if not (books_list is None):
            self.__books_list = books_list
        else:
            self.__books_list = []

        if not (employees_list is None):
            self.__employees_list = employees_list
        else:
            self.__employees_list = []

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_books(self):
        return self.__books_list

    def get_employees(self):
        return self.__employees_list

    def set_address(self, address):
        self.__address = address

    def add_book(self, book):
        if not isinstance(book, Book):
            raise Exception('Error type')

        if not (book in self.__books_list):
            self.__books_list.append(book)


    def remove_book(self, book):
        if not isinstance(book, Book):
            raise Exception('Error type')

        if book in self.__books_list:
            self.__books_list.remove(book)

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            raise Exception('Error type')

        if not (employee in self.__employees_list):
            self.__employees_list.append(employee)

    def remove_employee(self, employee):
        if not isinstance(employee, Employee):
            raise Exception('Error type')

        if employee in self.__employees_list:
            self.__employees_list.remove(employee)

    def __str__(self):
        return f'Имя: {self.__name}\n' \
               f'Адрес: {self.__address}\n' \
               f'Список книг: {self.__books_list}\n' \
               f'Список работников: {self.__employees_list}\n'
       

class Book:
    pass

class Employee:
    pass