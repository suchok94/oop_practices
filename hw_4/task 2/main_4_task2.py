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

    def __init__(self, title: str, author: str, year: int, id: int, genres: list[Genre] = None):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__id = id

        if not(genres is None):
            self.__genres = genres
        else:
            self.__genres = []

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_id(self):
        return self.__id

    def get_genres(self):
        return self.__genres

    def set_year(self, year):
        if not isinstance(year, int):
            raise Exception('Error type')

        if year > 0 and year < 2024:
            self.__year = year
        else:
            raise Exception("Error value")


    def add_genre(self, genre):
        if not isinstance(genre, Genre):
            raise Exception("Error type")

        if not (genre in self.__genres):
            self.__genres.append(genre)
        else:
            raise Exception("Error value")

    def remove_genre(self, genre):
        if not isinstance(genre, Genre):
            raise Exception("Error type")

        if genre in self.__genres:
            self.__genres.remove(genre)
        else:
            raise Exception("Error value")

    def __str__(self):
        return f'Tittle: {self.__title}\n' \
               f'Author: {self.__author}\n' \
               f'Year: {self.__year}\n' \
               f'id: {self.__id}\n' \
               f'Genres: {self.__genres}\n'

class Employee:

    def __init__(self, name: str, post: str, id: int, contact_info: list[ContactInfo] = None):
        self.__name = name
        self.__post = post
        self.__id = id

        if not (contact_info is None):
            self.__contact_info = contact_info
        else:
            self.__contact_info = []

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__post

    def get_id(self):
        return self.__id

    def get_contact_info(self):
        return self.__contact_info

    def set_position(self, position):
        self.__post = position

    def add_contact_info(self, type, value):
        contact_info = ContactInfo(type, value)
        self.__contact_info.append(contact_info)

    def remove_contact_info(self):
        self.__contact_info.clear()

    def __str__(self):
        return f'Name: {self.__name}\n' \
               f'Position: {self.__post}\n' \
               f'id: {self.__id}\n' \
               f'Contact Info: {self.__contact_info}\n'



class Genre:

    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def set_name(self, name: str):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def __str__(self):
        return f'Name: {self.__name}\n' \
               f'Description: {self.__description}\n'

class ContactInfo:

    def __init__(self, type: str, value: str):
        self.__type = type
        self.__value = value

    def get_type(self):
        return self.__type

    def get_description(self):
        return self.__value

    def set_type(self, type):
        self.__type = type

    def set_value(self, value):
        self.__value = value

    def __str__(self):
        return f'Type: {self.__type}\n' \
               f'Value: {self.__value}\n'

