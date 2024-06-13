from __future__ import annotations

import random
from random import randint

# task 4



class HogwartsStudent:

    def __init__(self, name: str, house: str, list_spells: list[Spell] = None, mana: int = 100):
         self.__name = name
         self.__house = house
         self.__mana = mana

         if not (list_spells is None):
            self.__list_speels = list_spells
         else:
            self.__list_speels = []


    def get_name(self):
        return self.__name

    def get_house(self):
        return self.__house

    def get_mana(self):
        return self.__mana

    def get_list_spells(self):
        return ", ".join(str(i.get_name()) for i in self.__list_speels)

    def set_name(self, name: str):
        self.__name = name

    def set_house(self, house: str):
        self.__house = house

    def set_mana(self, mana: int):
        self.__mana = mana

    def learn_spell(self, spell: Spell):
        self.__list_speels.append(spell)

    def cast_spell(self, enemy_student):
        i = randint(1, len(self.__list_speels)) - 1
        spell = self.__list_speels[i]
        print(f'{self.__name} выбирает заклинание {str(spell.get_name())}', end=' ')
        if self.__mana < spell.get_cost_mana():
            print(f'и ему не хватает маны на прокаст.\n'
                  f'Ход переходит к аппоненту')
        else:
            print(f'и кастует его')
            mana = self.__mana - spell.get_cost_mana()
            self.set_mana(mana)


    def __str__(self):
        return f'Name: {self.__name}\n' \
               f'House: {self.__house}\n' \
               f'Mana: {self.__mana}\n' \
               f'List of spells: {self.get_list_spells()}'


class Spell:

    def __init__(self, name: str, description: str, cost_mana: int):
        self.__name = name
        self.__description = description
        self.__cost_mana = cost_mana

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_cost_mana(self):
        return self.__cost_mana

    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def set_cost_mana(self, cost_mana):
        self.__cost_mana = cost_mana

    def __str__(self):
        return f'Name: {self.__name}\n' \
               f'Description: {self.__description}\n' \
               f'Cost mana: {self.__cost_mana}\n'

class Hogwarts:

    def __init__(self, students: list[HogwartsStudent], spells: list[Spell]):
        self.__students =students
        self.__spells = spells

    def get_students(self):
        return self.__students

    def get_spells(self):
        return self.__spells

    def enroll_student(self, student: HogwartsStudent):
        self.__students.append(student)

    def teach_spell(self, spell: Spell):
        self.__spells.append(spell)

    @staticmethod
    def simulate_duel(student1: HogwartsStudent, student2: HogwartsStudent):
        print('Битва началась')
        #while not (student1.get_mana() == 0) or not student2.get_mana() == 0:
        while True:
            student1.cast_spell(student2)
            print(student1.get_mana())
            # Hogwarts.check_mana(student1)
            if student1.get_mana() == 0:
                print(f'У {student1.get_name()} кончилась мана. Он проиграл')
                return False
            student2.cast_spell(student1)
            print(student2.get_mana())
            # Hogwarts.check_mana(student2)
            if student2.get_mana() == 0:
                print(f'У {student2.get_name()} кончилась мана. Он проиграл')
                return False

    # @staticmethod
    # def check_mana(student):
    #     if student.get_mana() == 0:
    #         return False
    #     else:
    #         return True

class Program:

    @staticmethod
    def main():
        student1 = HogwartsStudent('Harry', 'Griffindor')
        student2 = HogwartsStudent('Drako', 'Slizerith')
        spell1 = Spell('Expelliarmus', 'Дизармирование противника, низкая стоимость магической энергии.', 10)
        spell2 = Spell('Stupefy', 'Оглушение противника, средняя стоимость магической энергии.', 20)
        spell3 = Spell('Avada Kedavra', 'Смертельное ранение (используется редко), высокая стоимость магической энергии.', 30)
        spell4 = Spell('Protego', 'Защитный щит, отражающий заклинания, низкая стоимость магической энергии.', 10)
        spell5 = Spell('Petrificus Totalus', 'Полная парализация противника, средняя стоимость магической энергии.', 20)
        spell6 = Spell('Lumos', 'Создание источника света на конце волшебной палочки, низкая стоимость магической энергии.', 10)
        spell7 = Spell('Expecto Patronum', 'Призывание патронуса для защиты от дементоров, высокая стоимость магической энергии.', 30)

        student1.learn_spell(spell1)
        student1.learn_spell(spell2)
        student1.learn_spell(spell3)
        student1.learn_spell(spell4)
        student2.learn_spell(spell5)
        student2.learn_spell(spell6)
        student2.learn_spell(spell7)

        Hogwarts.simulate_duel(student1, student2)

Program.main()