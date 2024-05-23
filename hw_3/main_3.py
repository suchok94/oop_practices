from __future__ import annotations
class Wizard:

    def __init__(self, name: str, house: str, magic_level: int, list_spells: list[Spell], graduate: bool):
        self.__name = name
        self.__house = house
        self.__magic_level = magic_level
        self.__list_spells = list_spells
        self.__graduate = graduate

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
            self.__graduate == False
        else:
            raise Exception('Error message')

    




