from __future__ import annotations
class Wizard:

    def __init__(self, name: str, faculty: str, lvl_power: int, list_spells: list[Spell], graduate: bool):
        self.__name = name
        self.__facultu = faculty
        self.__lvl_power = lvl_power
        self.__list_spells = list_spells
        self.__graduate = graduate



