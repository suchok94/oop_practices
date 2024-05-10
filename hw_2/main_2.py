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

# task 5
class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z


    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)


    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return Vector(new_x, new_y, new_z)


    def __mul__(self, other):
        # if type(self) == float and type(other) == Vector:
        #     boof = self
        #     self = other
        #     other = boof
        if type(other) == int or type(other) == float:
            new_x = self.x * other
            new_y = self.y * other
            new_z = self.z * other
        elif type(self) == Vector and type(other) == Vector:
            new_x = self.y * other.z - self.z * other.y
            new_y = self.z * other.x - self.x * other.z
            new_z = self.x * other.y - self.y * other.x
        return Vector(new_x, new_y, new_z)


    @staticmethod
    def scalar_product(vec1, vec2):
        scalar = vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z
        return scalar

    def find_lenght(self):
        lenght =  (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        return lenght

    def __str__(self):
        return f'{self.x, self.y, self.z}'

# task 6
class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if Fraction.check_denominator(self, other):
            if self.denominator != other.denominator:
                boof = self.denominator
                self = self * other.denominator
                other = other * boof

            new_numerator = self.numerator + other.numerator
            return Fraction(new_numerator, self.denominator)

    def __sub__(self, other):
        if Fraction.check_denominator(self, other):
            if self.denominator != other.denominator:
                boof = self.denominator
                self = self * other.denominator
                other = other * boof
            new_numerator = self.numerator - other.numerator
            return Fraction(new_numerator, self.denominator)

    def __mul__(self, other):
        if Fraction.check_denominator(self, other):
            if type(self) == Fraction and type(other) == int:
                new_numerator = self.numerator * other
                new_denominator = self.denominator * other
            else:
                new_numerator = self.numerator * other.numerator
                new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)

    def check_denominator(self, other):
        if self.denominator == 0 or other.denominator == 0:
            print('В одном из знаменателе дробей "нуль"')
            return False
        return True

    def __str__(self):
        if self.numerator == self.denominator or self.denominator == 1:
            return f'{self.numerator/self.denominator}'
        else:
            return f'{self.numerator}/{self.denominator}'

#task 7
class GeometryUtils:
    PI = 3.14
    @staticmethod
    def find_square_circle(radius):
        square = GeometryUtils.PI * radius ** 2
        return square

    @staticmethod
    def find_perimeter_circle(radius):
        perimeter = 2 * GeometryUtils.PI * radius
        return perimeter

    @staticmethod
    def find_square_rectangle(length, width):
        square = length * width
        return square

    @staticmethod
    def find_perimeter_rectangle(length, width):
        perimeter = 2 * (length + width)
        return perimeter

    @staticmethod
    def find_square_triangle(length_a, length_b, length_c):
        if GeometryUtils.check_triangle(length_a, length_b, length_c):
            polu_perimeter = (length_a + length_b + length_c) / 2
            square = (polu_perimeter * (polu_perimeter - length_a) * (polu_perimeter - length_b) * (polu_perimeter - length_c)) ** 0.5
            return square
        else:
            return f'Такого треугольника не существует'

    @staticmethod
    def check_triangle(length_a, length_b, length_c):
        if length_a + length_b > length_c and length_a + length_c > length_b and length_b + length_c > length_a:
            return True


# task 8
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        Time.correct_time(self)




    def __add__(self, other):
        new_hour = self.hour + other.hour
        new_minute = self.minute + other.minute
        new_second = self.second + other.second
        sum_time = Time(new_hour, new_minute, new_second)
        return Time.correct_time(sum_time)

    def __sub__(self, other):
        sub_time = (self.hour * 3600 + self.minute * 60 + self.second) - (other.hour * 3600 + other.minute * 60 + other.second)
        time = Time(0, 0, sub_time)
        return Time.correct_time(time)

    def __mul__(self, other: int):
        new_hour = self.hour * other
        new_minute = self.minute * other
        new_second = self.second * other
        time = Time(new_hour, new_minute, new_second)
        return Time.correct_time(time)


    def correct_time(self):
        if abs(self.second) >= 60:
            self.minute = self.minute + self.second // 60
            self.second = self.second % 60
        if abs(self.minute) >= 60:
            self.hour = self.hour + self.minute // 60
            self.minute = self.minute % 60
        return self

    def __str__(self):

        return f'{self.hour:02}:{self.minute:02}:{self.second:02}'




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
        # lst = [[1,2,3],[4,5,6],[7,8,9]]
        # print(f'Сумма элементов массива: {ArrayUtils.sum_elements(lst)}')
        # print(f'Произведение элементов массива: {ArrayUtils.multi_elements(lst)}')
        # print(f'Инвертированный массив: {ArrayUtils.invert_array(lst)}')
        # print(f'Максимальный элемент массива: {ArrayUtils.find_max(lst)}')
        # print(f'Минимальный элемент массива: {ArrayUtils.find_min(lst)}')

        #task5
        # vec1 = Vector(1, 1, 1)
        # vec2 = Vector(1, -1, 5)
        # print(f'Первый вектор: {vec1}')
        # print(f'Второй вектор: {vec2}')
        # print(f'Сложение векторов: {vec1 + vec2}') # сложение векторов
        # print(f'Разница векторов: {vec1 - vec2}') # вычитание из первого вектора второго
        # print(f'Разница векторов: {vec2 - vec1}')  # вычитание из второго вектора первого
        # print(f'Скалярное произведение на скаляр: {vec1 * 123}') # скалярное произведение на int число
        # print(f'Скалярное произведение на скаляр: {vec2 * 3.14}')  # скалярное произведение на float число
        # # print(3.14 * vec2) # не работает, как я понял нужно править __mul__ в классе float?
        # print(f'Векторное произведение векторов: {vec1 * vec2}')  # вектороное произведение
        # print(f'Векторное произведение векторов: {vec2 * vec1}')  # вектороное произведение
        # print(f'Скалярное произведение двух векторов равно: {Vector.scalar_product(vec1, vec2)}')
        # print(f'Длина вектора {vec1} равна: {vec1.find_lenght()}')
        # print(f'Длина вектора {vec2} равна: {vec2.find_lenght()}')

        #task 6
        # fraction1 = Fraction(1,7)
        #
        # fraction2 = Fraction(2,2)
        # print(f'Первая дробь: {fraction1}')
        # print(f'Вторая дробь: {fraction2}')
        # print(f'Сумма этих дробей равна: {fraction1 + fraction2}')
        # print(f'Разница этих дробей равна: {fraction1 - fraction2}')
        # print(f'Разница этих дробей равна: {fraction2 - fraction1}')
        # print(f'Произведение этих дробей равна: {fraction1 * fraction2}')

        #task 7
        # radius_circle = int(input("Введите радиус круга: "))
        # print(f'Площадь круга: {GeometryUtils.find_square_circle(radius_circle)}')
        # print(f'Периметр круга: {GeometryUtils.find_perimeter_circle(radius_circle)}')
        # length_rectangle, width_rectangle = int(input("Введите одну сторону прямоугольника: ")), int(input("Введите другую сторону прямоугольника: "))
        # print(f'Площадь прямоугольник: {GeometryUtils.find_square_rectangle(length_rectangle, width_rectangle)}')
        # print(f'Периметр прямоугольника: {GeometryUtils.find_perimeter_rectangle(length_rectangle, width_rectangle)}')
        # side_a, side_b, side_c = int(input("Введите одну сторону треугольника: ")), int(input("Введите вторую сторону треугольника: ")), int(input("Введите третью сторону треугольника: "))
        # print(f'Площадь треугольника: {GeometryUtils.find_square_triangle(side_a, side_b, side_c)}')

        #task 8
        time1 = Time(1, 68, 100)
        time2 = Time(1, 121, 100)
        print(f'Первое время: {time1}')
        print(f'Второе время: {time2}')
        time3 = time2 + time1
        time4 = time2 - time1
        time5 = time1 - time2
        print(f'Сложение времени: {time3}')
        print(f'Разница второго и первого времени: {time4}')
        print(f'Разница первого и второго времени: {time5}')
        time6 = time1 * 5
        time7 = time2 * 3
        print(f'Первое время умноженное на 5: {time6}')
        print(f'Второе время умноженное на 3: {time7}')

Program.main()
