from __future__ import annotations
import datetime

# task 1
class Patient:

    def __init__(self, surname: str, name: str, patronymic: str, age: int, disease: str):
        '''
        Создаёт пациента
        :param surname:
        :param name:
        :param patronymic:
        :param age:
        :param disease:
        '''
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age
        self.disease = disease

    def make_an_appointment(self, date: date, time: time):
        """
        принимает дату и время приёма, выводит информацию о приёме
        :param date:
        :param time:
        :return:
        """
        print(f'Пациент {self.surname} {self.name} {self.patronymic} записан на приём {date} в {time}')

    def __str__(self):
        """
        Описывает информацию о пациенте
        :return: str, инфомарция о пациенте
        """
        return f'Информация о пациенте:\n' \
               f'ФИО: {self.surname} {self.name} {self.patronymic}\n' \
               f'Возраст: {self.age}\n' \
               f'Текущий диагноз: {self.disease}'

# task 2
class TouristSpot:
    def __init__(self, name: str, country: str, type: str, count_tourists: int = 0):
        '''
        Создаёт объект "Туристическая достопремечательность"
        :param name:
        :param country:
        :param type:
        '''
        self.name = name
        self.country = country
        self.type = type
        self.count_tourist = count_tourists

    def visit_spot(self, name_tourist: Tourist):
        '''
        Выводит сообщение о посещение туриста достопримечательности
        :param name_tourist:
        :return:
        '''
        print(f'Посетитель {name_tourist.surname} {name_tourist.name} посетил достопримечательность {self.name}')
        self.count_tourist += 1

    def __str__(self):
        '''
        Выводит информацию о туристической достопримечательности
        :return:
        '''
        return f'Информация о туристической достопримечательности:\n' \
               f'Название: {self.name}\n' \
               f'Страна расположения: {self.country}\n' \
               f'Тип достопримечательности: {self.type}\n' \
               f'Количество туристов которые посетили достопримечательность: {self.count_tourist}'

class Tourist:
    def __init__(self, surname: str, name: str):
        self.surname = surname
        self.name = name

# task 3
class ModelWindow:
    horizon_limit = 1960
    vertic_limit = 1080
    def __init__(self, name: str, coord_up_left: Vector2D, horizon_size: int, vertic_size: int, color: str, visibility_status: bool, frame_status: bool):
        self.name = name
        self.coord = coord_up_left
        self.horizon_size = horizon_size
        self.vertic_size = vertic_size
        self.color = color
        self.visibility_status = visibility_status
        self.frame_status = frame_status

    def move_window(self, new_x, new_y):
        if new_x + self.horizon_size <= ModelWindow.horizon_limit and new_y + self.vertic_size <= ModelWindow.vertic_limit:
            self.coord.x = new_x
            self.coord.y = new_y
        else:
            print("Невозможно задать такие координаты!")

    def change_size(self, new_horizon_size: int, new_vertic_size: int):
        if self.coord.x + new_horizon_size <= ModelWindow.horizon_limit and self.coord.y + new_vertic_size <= ModelWindow.vertic_limit:
            self.horizon_size = new_horizon_size
            self.vertic_size = new_vertic_size
        else:
            print("Невозможно задать такие размеры окна!")
    def change_color(self, new_color: str):
        self.color = new_color
    def change_status(self, new_visibility: bool, new_frame:bool ):
        self.visibility_status = new_visibility
        self.frame_status = new_frame
    def get_status(self):
        print(f'Состояние окна:\n'
              f'Видимость: {self.visibility_status}\n'
              f'Рамка: {self.frame_status}')
    def __str__(self):
        return f'Информация о окне:\n' \
               f'Название:{self.name}\n' \
               f'Координаты верхнего левого угла: {self.coord}\n' \
               f'Размер по горизонтали: {self.horizon_size}\n' \
               f'Размер по вертикали: {self.vertic_size}\n' \
               f'Цвет: {self.color}\n' \
               f'Состояние видимости: {"Видимое" if self.visibility_status else "Невидимое"}\n' \
               f'Состояние рамки: {"С рамкой" if self.frame_status else"Без рамки"}'

class Vector2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x= {self.x} y= {self.y} '

# task 4
class ArrayUtils:
    @staticmethod
    def sum_elements(array: list[list]):
        sum = 0
        for i in range(0, len(array), 1):
            for j in range(0, len(array[i]), 1):
                sum += array[i][j]
        return sum

    @staticmethod
    def multi_elements(array: list[list]):
        multiply = 1
        for i in range(0, len(array), 1):
            for j in range(0, len(array[i]), 1):
                multiply *= array[i][j]
        return multiply

    @staticmethod
    def invert_array(array: list[list]):
        for i in range(0, len(array) // 2, 1):
            for j in range(0, len(array[i]), 1):
                boof = array[i][j]
                array[i][j] = array[-i - 1][-j - 1]
                array[-i-1][-1-j] = boof
        return array

    @staticmethod
    def find_max(array: list[list]):
        max = array[0][0]
        for i in range(0, len(array), 1):
            for j in range(0, len(array[i]), 1):
                if max < array[i][j]:
                    max = array[i][j]
        return max

    @staticmethod
    def find_min(array: list[list]):
        min = array[0][0]
        for i in range(0, len(array), 1):
            for j in range(0, len(array[i]), 1):
                if min > array[i][j]:
                    min = array[i][j]
        return min
class Program:
    @staticmethod
    def main():
        """
        Запускает программу
        :return:
        """
        #task1
        # p1 = Patient('Petrov', 'Ivan', 'Ivanov', 20, 'computernaya zavisimost')
        # data = datetime.date(2024, 5, 11)
        # time = datetime.time(2, 20)
        # p1.make_an_appointment(data, time)
        # print(p1.__str__())

        #task2
        # tourist1 = Tourist('Petrov', 'Petya')
        # tourist2 = Tourist('Ivanov', 'Vanya')
        # spot1 = TouristSpot('Mamaev Kurgan', 'Russia', 'Историческая')
        # spot1.visit_spot(tourist1)
        # spot1.visit_spot(tourist2)
        # print(spot1.__str__())

        #task3
        # coord1 = Vector2D(0,0) # создание объекта Вектор, который содержит точки левого верхнего угла окна
        # window1 = ModelWindow('nazvanie', coord1, 100, 100, 'blue', True, False) # создание объекта окно
        # print(window1) # первоначальная информация об объекте
        # new_x, new_y = int(input("Введите новые координаты левого верхнего угла окна (x): ")), int(input("(y): "))
        # window1.move_window(new_x, new_y)
        # new_horizon, new_vertical = int(input("Введите новые размеры по горизонтали: ")), int(input("по вертикали: "))
        # window1.change_size(new_horizon, new_vertical)
        # new_color = input('Введите новый цвет: ')
        # window1.change_color(new_color)
        # new_visibility = input('Введите статус видимости окна (видимое\невидимое): ')
        # new_frame = input('Введите статус рамки окна (с рамкой\без рамки): ')
        # window1.change_status(True if new_visibility == 'видимое' else False, True if new_frame == 'с рамкой' else False)
        # print(window1) # изменённая информация об объекте

        #task4
        lst = [[1,2,3],[4,5,6],[7,8,9]]
        print(f'Сумма элементов массива: {ArrayUtils.sum_elements(lst)}')
        print(f'Произведение элементов массива: {ArrayUtils.multi_elements(lst)}')
        print(f'Инвертированный массив: {ArrayUtils.invert_array(lst)}')
        print(f'Максимальный элемент массива: {ArrayUtils.find_max(lst)}')
        print(f'Минимальный элемент массива: {ArrayUtils.find_min(lst)}')
Program.main()
