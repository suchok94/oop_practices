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


class Program:
    @staticmethod
    def main():
        """
        Запускает программу
        :return:
        """
        p1 = Patient('Petrov', 'Ivan', 'Ivanov', 20, 'computernaya zavisimost')
        data = datetime.date(2024, 5, 11)
        time = datetime.time(2, 20)
        p1.make_an_appointment(data, time)
        print(p1.__str__())

Program.main()
