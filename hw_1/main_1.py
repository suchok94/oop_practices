# task № 1
class Animal:
    def __init__(self, name: str, type: str, age: int, sound: str):
        self.name = name
        self.type = type
        self.age = age
        self.sound = sound

    def sound_animal(self):
        print(f'Животное с именем {self.name} издаёт звук: "{self.sound}"\n')

    def info_of_animal(self):
        print(f'Имя животного: {self.name}')
        print(f'Вид животного: {self.type}')
        print(f'Его возраст: {self.age}')
        print("")

class Program:

    @staticmethod
    def main():
        animal1 = Animal('Kesha', 'Popugai', 14, 'PopkaDurak')
        animal1.sound_animal()
        animal1.info_of_animal()

        animal2 = Animal('Snoop', 'Dog', 7, 'WoofWoof')
        animal2.sound_animal()
        animal2.info_of_animal()


Program.main()

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
        book1 = Book('The Martian Chronicles', 'Ray Bradbury', 604)

        book1.info_about_book()
        pages_open_book = int(input("Введите номер страницы на которой открыть книгу: "))
        book1.open_book(pages_open_book)

Program.main()

# task № 3
class PassengerPlane:
        def __init__(self, manufacturer: str, model: str, capacity: int, current_height: float, current_speed: float):
            self.manufacturer = manufacturer
            self.model = model
            self.capacity = capacity
            self.height = current_height
            self.speed = current_speed

        def take_off_plane(self):
            print(f'Самолёт {self.manufacturer}{self.model} взлетел!')

        def landing_plane(self):
            print(f'Самолёт {self.manufacturer}{self.model} приземлился!')

        def change_height(self, height):
            self.height = height

        def change_speed(self, speed):
            self.speed = speed

        def info_about_plane(self):
            print(f'Информация о самолёте: {self.manufacturer} {self.model}.\nВместимость самолёта: {self.capacity}\nТекущая высота:{self.height}\nТекущая скорость:{self.speed}')

