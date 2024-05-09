import datetime
# task 1
class Patient:

    def __init__(self, surname: str, name: str, patronymic: str, age: int, disease: str):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age
        self.disease = disease

    def make_an_appointment(self, date: date, time: date):
        print(f'Пациент {self.surname} {self.name} {self.patronymic} записан на приём {date} в {time}')

    def __str__(self):
        return f'Информация о пациенте:' \
               f'ФИО: {self.surname, self.name, self.patronymic}' \
               f'Возраст: {self.age}' \
               f'Текущий диагноз: {self.disease}'
    


