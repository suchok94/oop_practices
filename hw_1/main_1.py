# task № 1
class Animal:
    def __init__(self, name: str, type: str, age: int, sound: str):
        self.name = name
        self.type = type
        self.age = age
        self.sound = sound


    def sound_animal(self):
        print(f'Животное с именем {self.name} издаёт звук: "{self.sound}"\n')

    def info_of_animal(self):
        print(f'Имя животного: {self.name}')
        print(f'Вид животного: {self.type}')
        print(f'Его возраст: {self.age}')
        print("")

class Program:

    @staticmethod
    def main():
        animal1 = Animal('Kesha', 'Popugai', 14, 'PopkaDurak')
        animal1.sound_animal()
        animal1.info_of_animal()

        animal2 = Animal('Snoop', 'Dog', 7, 'WoofWoof')
        animal2.sound_animal()
        animal2.info_of_animal()

Program.main()