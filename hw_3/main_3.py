from __future__ import annotations
# task 1
class Wizard:


    def __init__(self, name: str, house: str, magic_level: int, graduate: bool, list_spells: list[Spell] = None):
        self.__name = name
        self.__house = house
        self.__magic_level = magic_level
        self.__graduate = graduate

        if list_spells is None:
            self.__list_spells = []
        else:
            self.__list_spells = list_spells


    def get_name(self):
        return self.__name

    def get_house(self):
        return self.__house

    def get_magic_level(self):
        return self.__magic_level

    def get_spells(self):
        return self.__list_spells

    def get_status(self):
        return self.__graduate

    def set_house(self, house: str):
        self.__house = house


    def set_magic_level(self, magic_level: int):
        if not isinstance(magic_level, int):
            raise Exception("magic level isn't int")

        if magic_level > 0:
            self.__magic_level = magic_level
        else:
            raise Exception("magic level <= 0")

    def set_status(self, status: str):
        if status.lower() == 'выпущен':
            self.__graduate = True
        elif status.lower() == 'в хогвартсе':
            self.__graduate = False
        else:
            raise Exception('Error message')

    def add_spell(self, spell: Spell):
        if not(spell in self.__list_spells):
            self.__list_spells.append(spell)


    def remove_spell(self, spell: Spell):
        if spell in self.__list_spells:
            self.__list_spells.remove(spell)


    def increase_magic_level(self, amount: int):
        if not isinstance(amount, int):
            raise Exception("amount isn't int")

        if amount > 0:
            self.__magic_level += amount
        else:
            raise Exception("amount <=0")

    def __str__(self):
        return f'Имя волшебника: {self.__name}' \
               f'Факултет: {self.__house}' \
               f'Уровень магической силы: {self.__magic_level}' \
               f'Список известных заклинаний: {self.__list_spells}' \
               f'Статус выпуска: {self.__graduate}'

class Spell:

    def __init__(self, name: str, difficulty: int, type: str, description: str):
        self.__name = name
        self.__difficulty = difficulty
        self.__type = type
        self.__description = description

    def get_name(self):
        return self.__name

    def get_difficulty(self):
        return self.__difficulty

    def get_type(self):
        return self.__type

    def get_description(self):
        return self.__description

    def set_name(self, name: str):
        self.__name = name

    def set_difficulty(self, difficulty: int):
        if not isinstance(difficulty, int)
            raise Exception("Difficulty isn't int")

        if difficulty > 0 and difficulty < 10:
            self.__difficulty = difficulty
        else:
            raise Exception("Error value")

    def set_type(self, type: str):
        self.__type = type


    def set_description(self, description: str):
        self.__description = description

    def __str__(self):
        return f'Название {self.__name}' \
               f'Уровень сложности: {self.__difficulty}' \
               f'Тип: {self.__type} ' \
               f'Описание: {self.__description}'


class Program:

    @staticmethod
    def main():
        pass


Program.main()