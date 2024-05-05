# task № 1
class Animal:
    def __init__(self, name: str, type: str, age: int, sound: str):
        self.name = name
        self.type = type
        self.age = age
        self.sound = sound


    def sound_animal(self):
        print(f'Животное с именем {self.name} издаёт звук: "{self.sound}"')

    def info_of_animal(self):
        print(f'Имя животного: {self.name}')
        print(f'Вид животного: {self.type}')
        print(f'Его возраст: {self.age}')
        

