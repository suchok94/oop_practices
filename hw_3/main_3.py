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

# # task 2
# class Employee:
#
#     def __init__(self, name: str, position: str, department: str, salary: float, length_of_service: int,
#                  list_completed_projects: list[Project] = None) -> object:
#         self.__name = name
#         self.__position = position
#         self.__department = department
#         self.__salary = salary
#         self.__length_of_service = length_of_service
#
#         if not(list_completed_projects is None):
#             self.__list_completed_projects = list_completed_projects
#         else:
#             self.__list_completed_projects = []
#
#     def add_completed_project(self, project):
#         if not (project in self.__list_completed_projects):
#             self.__list_completed_projects.append(project)
#
#     def remove_completed_project(self, project):
#         if project in self.__list_completed_projects:
#             self.__list_completed_projects.remove(project)
#
#     def increase_salary(self, addition):
#         if addition > 0:
#             self.__salary += addition
#         else:
#             raise Exception('Error value')
#
#     def get_name(self):
#         return self.__name
#
#     def get_position(self):
#         return self.__position
#
#     def get_department(self):
#        return self.__department
#
#     def get_salary(self):
#         return self.__salary
#
#     def get_length_of_service(self):
#         return self.__length_of_service
#
#     def get_list_completed_projects(self):
#         return self.__list_completed_projects
#
#     def set_name(self, name: str):
#         self.__name = name
#
#     def set_position(self, position: str):
#         self.__position = position
#
#     def set_department(self, department: str):
#         self.__department = department
#
#     def set_salary(self, salary: float):
#         if not isinstance(salary, float):
#             raise Exception("Error type")
#
#         if salary > 0:
#             self.__salary = salary
#         else:
#             raise Exception("Error value")
#
#     def set_length_of_service(self, length_of_service: int):
#         if not(isinstance(length_of_service, int)):
#             raise Exception("Error type")
#
#         if length_of_service >= 0:
#             self.__length_of_service = length_of_service
#         else:
#             raise Exception("Error value")
#
#     def __str__(self):
#         return f'Имя сотрудника: {self.__name}\n' \
#                f'Должность: {self.__position}\n' \
#                f'Отдел: {self.__department}\n' \
#                f'Зарплата: {self.__salary}\n' \
#                f'Стаж работы: {self.__length_of_service}\n' \
#                f'Список выполненных проектов: {", ".join(str(name.get_name()) for name in self.__list_completed_projects)}\n'
#
# class Project:
#
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name

# # task 3
# class Robot:
#
#     def __init__(self, serial_number: str, model: str, current_task: str, battery_charge_level: int, status_work: bool):
#         self.__serial_number = serial_number
#         self.__model = model
#         self.__current_task = current_task
#         self.__battery_charge_level = battery_charge_level
#         self.__status_work = status_work
#
#     def new_task(self, task: str):
#         self.__current_task = task
#
#     def change_battery_charge_level(self, battery_charge_level: int):
#         if not isinstance(battery_charge_level, int):
#             raise Exception('Error type')
#
#         if battery_charge_level >= 0 and battery_charge_level <= 100:
#             self.__battery_charge_level = battery_charge_level
#         else:
#             raise Exception('Error value')
#
#     def working(self):
#         self.__status_work = True
#
#     def dont_working(self):
#         self.__status_work = False
#
#     def get_serial_number(self):
#         return self.__serial_number
#
#     def get_model(self):
#         return self.__model
#
#     def get_current_task(self):
#         return self.__current_task
#
#     def get_battery_charge_level(self):
#         return self.__battery_charge_level
#
#     def get_status_work(self):
#         return self.__status_work
#
#     def set_serial_number(self, serial_number: str):
#         self.__serial_number = serial_number
#
#     def set_model(self, model: str):
#         self.__model = model
#
#     def __str__(self):
#         return f'Робот:' \
#                f'Серийный номер: {self.__serial_number}\n' \
#                f'Модель: {self.__model}\n' \
#                f'Текущая задача: {self.__current_task}\n' \
#                f'Уровень заряда батареи: {self.__battery_charge_level}\n' \
#                f'Статус работы: {self.__status_work}\n'

# task 4
class Athlete:

    def __init__(self, name: str, age: int, type_of_sport: str, list_achivments: list[Achivment], active_status: bool):

        pass


class Achivment:

    def __init__(self):
        pass

class Program:

    @staticmethod
    def main():
        # # task 1
        # wiz1 = Wizard('Vasya', 'Griff', 3, True)
        # spell1 = Spell('Abrakadabra', 1, 'Creating', 'Create new life')
        # spell2 = Spell('SimSalabim', 1, 'Destroy', 'Destroing object')
        # wiz1.add_spell(spell1)
        # wiz1.add_spell(spell2)
        # print(wiz1)
        # print(spell1)
        # wiz1.remove_spell(spell1)
        # print(wiz1)

        # # task 2
        # emp1 = Employee("Ivan", "Jun", "IT", 123, 1)
        # project1 = Project('Yandex')
        # project2 = Project('Google')
        #
        # emp1.add_completed_project(project1)
        # emp1.add_completed_project(project2)
        #
        # print(emp1)

        # # task 3
        # robot1 = Robot('1c22da123', 'T1000', 'Kill John Konner', 100, True)
        # print(robot1)
        # robot1.new_task('Грузить картошку')
        # robot1.change_battery_charge_level(0)
        # robot1.dont_working()
        # print(robot1)

Program.main()