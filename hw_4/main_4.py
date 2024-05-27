# task 1
class Student:

    def __init__(self,
                 name: str,
                 surname: str,
                 age: int,
                 avg_score: float):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__avg_score = avg_score

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def get_avg_score(self):
        return self.__avg_score

    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

    def set_age(self, age):
        if not isinstance(age, int):
            raise Exception("Error type")

        if age > 14 and age < 100:
            self.__age = age
        else:
            raise Exception("Error value")

    def set_avg_score(self, avg_score):
        if not isinstance(avg_score, float):
            raise Exception("Error type")

        if avg_score >= 1 and avg_score <= 5:
            self.__avg_score = avg_score
        else:
            raise Exception("Error value")

    def __str__(self):
        return f'Имя студента: {self.__name}\n' \
               f'Фамилия: {self.__surname}\n' \
               f'Возраст: {self.__age}\n' \
               f'Средний балл: {self.__avg_score}\n'

    
