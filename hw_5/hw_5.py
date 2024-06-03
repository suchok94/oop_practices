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




# # task 2
# class Person:
#
#     _name: str
#     _age: int
#
#     def __init__(self, name: str, age: int):
#         self._name = name
#         self._age = age
#
#     def introduce_yourself(self):
#         print(f'Name: {self._name}\n'
#               f'Age: {self._age}')
#
#
# class Doctor(Person):
#
#     def __init__(self, name: str, age: int, specialization: str):
#         Person.__init__(self, name, age)
#         self.__specialization = specialization
#
#     def introduce_yourself(self):
#         Person.introduce_yourself(self)
#         print(f'Specialization: {self.__specialization}')
#
# class Engineer(Person):
#
#     def __init__(self, name: str, age: int, grade: int):
#         Person.__init__(self, name, age)
#         self.__grade = grade
#
#     def introduce_yourself(self):
#         Person.introduce_yourself(self)
#         print(f'Grade: {self.__grade}')
#
# class Artist(Person):
#
#     def __init__(self, name: str, age: int, genre: str):
#         Person.__init__(self, name, age)
#         self.__genre = genre
#
#     def introduce_yourself(self):
#         Person.introduce_yourself(self)
#         print(f'Grade: {self.__genre}')

# task 3
class Transport_Means:
        pass

class Train(Transport_Means):
    pass

class Express(Train):
    pass

class Car(Transport_Means):
    pass


# task 4

class Animal:
    pass

class Fish(Animal):
    pass

class Mammals(Animal):
    pass

class Cat(Mammals):
    pass

class Dog(Mammals):
    pass

class Shark(Fish):
    pass

class Karp(Fish):
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

        # # task2
        # doctor1 = Doctor('Aibolit', 60, 'Vet')
        # engineer1 = Engineer('Mihalich', 55, 6)
        # artist1 = Artist('Jim Kerry', 50, 'Comedy')
        # doctor1.introduce_yourself()
        # engineer1.introduce_yourself()
        # artist1.introduce_yourself()



Program.main()