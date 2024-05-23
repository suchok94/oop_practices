from __future__ import annotations
# task 1
# class Wizard:
#
#
#     def __init__(self, name: str, house: str, magic_level: int, graduate: bool, list_spells: list[Spell] = None):
#         self.__name = name
#         self.__house = house
#         self.__magic_level = magic_level
#         self.__graduate = graduate
#
#         if list_spells is None:
#             self.__list_spells = []
#         else:
#             self.__list_spells = list_spells
#
#
#     def get_name(self):
#         return self.__name
#
#     def get_house(self):
#         return self.__house
#
#     def get_magic_level(self):
#         return self.__magic_level
#
#     def get_spells(self):
#         return self.__list_spells
#
#     def get_status(self):
#         return self.__graduate
#
#     def set_house(self, house: str):
#         self.__house = house
#
#
#     def set_magic_level(self, magic_level: int):
#         if not isinstance(magic_level, int):
#             raise Exception("magic level isn't int")
#
#         if magic_level > 0:
#             self.__magic_level = magic_level
#         else:
#             raise Exception("magic level <= 0")
#
#     def set_status(self, status: str):
#         if status.lower() == 'выпущен':
#             self.__graduate = True
#         elif status.lower() == 'в хогвартсе':
#             self.__graduate = False
#         else:
#             raise Exception('Error message')
#
#     def add_spell(self, spell: Spell):
#         if not(spell in self.__list_spells):
#             self.__list_spells.append(spell)
#
#
#     def remove_spell(self, spell: Spell):
#         if spell in self.__list_spells:
#             self.__list_spells.remove(spell)
#
#
#     def increase_magic_level(self, amount: int):
#         if not isinstance(amount, int):
#             raise Exception("amount isn't int")
#
#         if amount > 0:
#             self.__magic_level += amount
#         else:
#             raise Exception("amount <=0")
#
#     def __str__(self):
#         return f'Имя волшебника: {self.__name}\n' \
#                f'Факултет: {self.__house}\n' \
#                f'Уровень магической силы: {self.__magic_level}\n' \
#                f'Список известных заклинаний: {", ".join(str(i.get_name()) for i in self.__list_spells)} \n'\
#                f'Статус выпуска: {self.__graduate}\n'
#
# class Spell:
#
#     def __init__(self, name: str, difficulty: int, type: str, description: str):
#         self.__name = name
#         self.__difficulty = difficulty
#         self.__type = type
#         self.__description = description
#
#     def get_name(self):
#         return self.__name
#
#     def get_difficulty(self):
#         return self.__difficulty
#
#     def get_type(self):
#         return self.__type
#
#     def get_description(self):
#         return self.__description
#
#     def set_name(self, name: str):
#         self.__name = name
#
#     def set_difficulty(self, difficulty: int):
#         if not isinstance(difficulty, int):
#             raise Exception("Difficulty isn't int")
#
#         if difficulty > 0 and difficulty < 10:
#             self.__difficulty = difficulty
#         else:
#             raise Exception("Error value")
#
#     def set_type(self, type: str):
#         self.__type = type
#
#
#     def set_description(self, description: str):
#         self.__description = description
#
#     def __str__(self):
#         return f'Название {self.__name}\n' \
#                f'Уровень сложности: {self.__difficulty}\n' \
#                f'Тип: {self.__type}\n' \
#                f'Описание: {self.__description}\n'

# task 2
class Employee:

    def __init__(self, name: str, position: str, department: str, salary: float, length_of_service: int, list_completed_projects: list[Project] = None):
        self.__name = name
        self.__position = position
        self.__department = department
        self.__salary = salary
        self.__length_of_service = length_of_service

        if not(list_completed_projects is None):
            self.__list_completed_projects = list_completed_projects
        else:
            self.__list_completed_projects = []

    def add_completed_project(self):
        pass

    def remove_completed_project(self):
        pass

    def increase_salary(self):
        pass

    def get_name(self):
        pass

    def get_position(self):
        pass

    def get_department(self):
        pass

    def get_salary(self):
        pass

    def get_length_of_service(self):
        pass

    def get_list_completed_projects(self):
        pass

    def set_name(self):
        pass

    def set_position(self):
        pass

    def set_department(self):
        pass

    def set_salary(self):
        pass

    def set_length_of_service(self):
        pass

    

class Program:

    @staticmethod
    def main():
        wiz1 = Wizard('Vasya', 'Griff', 3, True)
        spell1 = Spell('Abrakadabra', 1, 'Creating', 'Create new life')
        spell2 = Spell('SimSalabim', 1, 'Destroy', 'Destroing object')
        wiz1.add_spell(spell1)
        wiz1.add_spell(spell2)
        print(wiz1)
        print(spell1)
        wiz1.remove_spell(spell1)
        print(wiz1)


Program.main()