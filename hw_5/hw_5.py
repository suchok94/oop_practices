# task 1

class Animal:

    _name: str
    _species: str

    def __init__(self, name: str, species: str):
        self._name = name
        self._species = species

    def make_sound(self):
        return f'Animal make sound'


