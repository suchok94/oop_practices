from __future__ import annotations
class Wizard:

    def __init__(self, name: str, faculty: str, lvl_power: int, list_spells: list[Spell], graduate: bool):
        self.__name = name
        self.__faculty = faculty
        self.__lvl_power = lvl_power
        self.__list_spells = list_spells
        self.__graduate = graduate

    def get_name(self):
        return self.__name

    def get_house(self):
        return self.__faculty

    def get_magic_level(self):
        return self.__lvl_power

    def get_spells(self):
        return self.__list_spells

    def get_status(self):
        return self.__graduate
    



