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
        tourist1 = Tourist('Petrov', 'Petya')
        tourist2 = Tourist('Ivanov', 'Vanya')
        spot1 = TouristSpot('Mamaev Kurgan', 'Russia', 'Историческая')
        spot1.visit_spot(tourist1)
        spot1.visit_spot(tourist2)
        print(spot1.__str__())

Program.main()
