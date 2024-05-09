from __future__ import annotations
import datetime

# task 1
class Patient:

    def __init__(self, surname: str, name: str, patronymic: str, age: int, disease: str):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age
        self.disease = disease

    def make_an_appointment(self, date: date, time: time):
        print(f'Пациент {self.surname} {self.name} {self.patronymic} записан на приём {date} в {time}')

    def __str__(self):
        return f'Информация о пациенте:\n' \
               f'ФИО: {self.surname} {self.name} {self.patronymic}\n' \
               f'Возраст: {self.age}\n' \
               f'Текущий диагноз: {self.disease}'


class Program:
    @staticmethod
    def main():

