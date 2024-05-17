from __future__ import annotations

# task 1
# class Car:
#
#     def __init__(self, brand: str, model: str, year: int, color: str, mileage: float, status: bool, speed: float):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color
#         self.mileage = mileage
#         self.status = status
#         self.speed = speed
#
#     def start_engine(self):
#         if not self.status:
#             self.status = True
#
#     def stop_engine(self):
#         if self.status:
#             self.status = False
#
#     def set_speed(self, speed: float):
#         if not isinstance(speed, float):
#             raise Exception('Error')
#
#         if speed >= 0 and speed < 200:
#             self.speed = speed
#
#     def set_color(self, color):
#         self.color = color
#
#     def get_status(self):
#         return self.status
#
#     def get_speed(self):
#         return self.speed
#
#     def get_mileage(self):
#         return self.mileage
#
#     def __str__(self):
#         return (f'Автомобиль: {self.brand} {self.model}\n'
#                 f'Год выпуска: {self.year}\n'
#                 f'Цвет: {self.color}\n'
#                 f'Пробег: {self.mileage}\n'
#                 f'Заведён: {self.status}\n'
#                 f'Текущая скорость: {self.speed}')
#

# # task 2
# class Smartphone:
#
#     def __init__(self, brand: str, model: str, system: str, storage: int, free_memory: float, ram: int, battery_charge: int, status: bool, app_list: list = []):
#         self.brand = brand
#         self.model = model
#         self.system = system
#         self.storage = storage
#         self.free_memory = free_memory
#         self.ram = ram
#         self.battery_charge = battery_charge
#         self.status = status
#         self.app_list = app_list
#
#
#
#
#     def on(self):
#         if not self.status:
#             self.status = True
#
#     def off(self):
#         if self.status:
#             self.status = False
#
#     def set_system(self, new_system):
#         self.system = new_system
#
#     def install_app(self, app):
#         size = int(app.get_size())
#         name = app.get_name()
#
#         if size + self.free_memory < self.storage:
#             print(f'Приложение {name} успешно установлено!')
#             self.free_memory += size
#             self.app_list.append(name)
#         else:
#             print(f'Памяти не хватает')
#
#     def unistall_app(self, app):
#         name = app.get_name()
#         if name in self.app_list:
#             self.free_memory -= int(app.get_size())
#             self.app_list.remove(name)
#             print(f'Приложение {name} успешно удалено!')
#
#
#     def set_battery_charge(self, new_battery_charge):
#         self.battery_charge = new_battery_charge
#
#     def get_status(self):
#         return self.status
#
#     def get_battery_charge(self):
#         return self.battery_charge
#
#     def __str__(self):
#         return (f'Смартфон: {self.brand} {self.model}\n'
#                 f'Операционная система: {self.system}\n'
#                 f'Встроенная память: {self.storage}\n'
#                 f'Свободное место: {self.free_memory}\n'
#                 f'Объём оперативной памяти: {self.ram}\n'
#                 f'Заряд процентов: {self.battery_charge}\n'
#                 f'Состояние: {self.status}\n'
#                 f'Список приложений: {self.app_list}')


# class App:
#
#     def __init__(self, name, size: int):
#         self.name = name
#         self.size = size
#
#     def get_size(self):
#         return self.size
#
#     def get_name(self):
#         return self.name

# task 3
class Potion:

    def __init__(self, name: str, ingredients: list[str], difficulty_making: int,  effect: str, status_making: bool):
        self.name = name
        self.ingredients = ingredients
        self.difficulty_making = difficulty_making
        self.effects = effect
        self.status_making = status_making

    def add_ingredient(self, new_ingredient):
        self.ingredients.append(new_ingredient)

    def del_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)

    def set_difficulty_making(self, new_difficulty):
        if isinstance(new_difficulty, int):
            self.difficulty_making = new_difficulty

    def making(self):
        if not self.status_making:
            self.status_making = True

    def change_effect(self, new_effect):
        self.effects = new_effect

    def get_is_making(self):
        return self.status_making

    def get_list_ingredient(self):
        return str(self.ingredients)

    def __str__(self):
        return f'Информация о зелье\n' \
               f'Название: {self.name}\n' \
               f'Список ингридиентов: {self.get_list_ingredient()}\n' \
               f'Сложность приготовления: {self.difficulty_making}\n' \
               f'Эффект: {self.effects}\n' \
               f'Состояние приготовления: {self.status_making}\n'



# task 4
class Library:
    def __init__(self, name: str, adress: str, list_books: list[Book] = None, list_users: list[User] = None):
        self.name = name
        self.name = adress

        if list_books is None:
            self.list_books = []
        else:
            self.list_books = list_books

        if list_users is None:
            self.list_users = []
        else:
            self.list_users = list_users

    def add_book(self, book: Book):
        if not book in self.list_books:
            self.list_books.append(book)

    def remove_book(self, book: Book):
        if book in self.list_books:
            self.list_books.remove(book)

    def register_user(self, user: User):
        if not user in self.list_users:
            self.list_users.append(user)

    def issue_book(self, book: Book, user: User):
        if book.is_available:
            user.list_books.append(book)
            book.set_available(False)
            book.set_current_user(user.name)

    def return_book(self, book: Book, user: User):
        if book in user.list_books:
            book.set_available(True)
            user.list_books.remove(book)
            book.set_current_user(None)

    def get_books_status(self):
        # info = ''
        # for i in self.list_books:
        #     info += f'{Book.get_status(i)}\n\n'
        # info = info for info in Book.get_status(info)
        return '\n'.join(str(item) for item in self.list_books)



    def get_users_status(self):
        # info = ''
        # for i in self.list_users:
        #     info += f'{User.get_info_user(i)}'
        # return info
        return '\n'.join(str(i) for i in self.list_users)


class Book:
    def __init__(self, name: str, author: str, year: int, genre: str, availability: bool):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.availability = availability
        self.current_user = None

    def is_available(self):
        return self.availability

    def set_available(self, availability):
        self.availability = availability

    def get_status(self):
        return f'Название книги: {self.name}\n' \
               f'Автор: {self.author}\n' \
               f'Доступность: {self.availability}\n' \
               f'Текущий пользователь: {self.current_user}\n'

    def set_current_user(self, name_user):
        if name_user is None:
            self.current_user = None
        else:
            self.current_user = name_user



    def __str__(self):
        return f'Info about book\n' \
               f'name: {self.name}\n' \
               f'author: {self.author}\n' \
               f'year: {self.year}\n' \
               f'genre: {self.genre}\n' \
               f'availaability: {self.availability}\n'


class User:
    def __init__(self, name, id_ticket, list_books: list[Book] = None):
        self.name = name
        self.id_ticket = id_ticket

        if list_books is None:
            self.list_books = []
        else:
            self.list_books = list_books

    def get_list_book(self):
        info = '|'
        for i in self.list_books:
            i = i.name
            info += f' {str(i)} |'
        return info

    def __str__(self):
        return f'Информация о пользователе\n' \
               f'Имя пользователя: {self.name}\n' \
               f'Номер читательского билета: {self.id_ticket}\n' \
               f'Список взятых книг:' \
               f'{self.get_list_book()}\n'


class Program:
    @staticmethod
    def main():
        # car1 = Car("Vaz", '2104',  1995, "Blue", 390000, False, 0)
        # car1.set_speed(45.0)
        # car1.start_engine()
        # car1.stop_engine()
        # print(car1.get_status())
        # print(car1.get_speed())
        # print(car1)

        # phone1 = Smartphone("Nokia", "3310", 'abc', 64, 62, 8, 59, True)
        # app1 = App("Ecxel", 1)
        # phone1.set_system('qwerty')
        # phone1.install_app(app1)
        # print(phone1)
        # phone1.unistall_app(app1)
        # print(phone1)

        # libr = Library('Lenina', 'st Lenina')
        # book1 = Book('Skazka', 'People', 2000, 'People story', True)
        # book2 = Book('It', 'King', 1980, 'Scary', True)
        # print(book1)
        # libr.add_book(book1)
        # libr.add_book(book2)
        # print(libr.get_books_status())

        # zelie1 = Potion('Romashka', ['Ромашка', 'Мухомор', 'Чайный гриб'], 1, 'Повышает ХП', False)
        # print(zelie1)
        # zelie1.add_ingredient('Камень')
        # zelie1.del_ingredient('Ромашка')
        # zelie1.set_difficulty_making(3)
        # zelie1.making()
        # zelie1.change_effect('Вызывает несварение')
        # print(f'Статус приготовления: {zelie1.get_is_making()}\n')
        # print(f'Список ингридиентов: {zelie1.get_list_ingredient()}\n')
        # print(zelie1)

        libr = Library('Lenina', 'st Lenina')
        book1 = Book('Skazka', 'People', 2000, 'People story', True)
        book2 = Book('It', 'King', 1980, 'Scary', True)
        user1 = User('Ivan', 1)
        user2 = User('Petr', 2)
        libr.register_user(user1)
        libr.register_user(user2)
        print(libr.get_books_status())
        libr.issue_book(book1, user1)
        libr.issue_book(book2, user1)
        # print(book1)
        libr.add_book(book1)
        libr.add_book(book2)
        print(book1.get_status())
        print(libr.get_users_status())
        print(libr.get_books_status())
        print(libr.get_users_status())
        libr.return_book(book1, user1)
        print(libr.get_books_status())
        print(libr.get_users_status())


Program.main()
