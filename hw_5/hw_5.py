# # task 1
#
# class Animal:
#
#     _name: str
#     _species: str
#
#     def __init__(self, name: str, species: str):
#         self._name = name
#         self._species = species
#
#     def make_sound(self):
#         return f'Animal make sound'
#
#
# class Dog(Animal):
#
#     def __init__(self, name: str, species: str):
#         Animal.__init__(self, name, species)
#
#     def make_sound(self):
#         return f'Dog make Woof'
#
#
# class Cat(Animal):
#     def make_sound(self):
#         return f'Cat make Meow'
#
#
# class Bird(Animal):
#     def make_sound(self):
#         return f'Bird make ChirikChirik'




# task 2
class Person:

    _name: str
    _age: int

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def introduce_yourself(self):
        pass

    

class Program:

    @staticmethod
    def main():
        # # task1
        # dog1 = Dog('Bobik', 'Recks')
        # cat1 = Cat('Murka', 'Siamskaya')
        # bird1 = Bird('Kesha', 'Popugai')
        #
        # print(dog1.make_sound())
        # print(cat1.make_sound())
        # print(bird1.make_sound())


Program.main()