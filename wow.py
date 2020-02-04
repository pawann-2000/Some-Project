# Users
# Archers, Ogers, Wizards


class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('Do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'Attacking with the power of {self.power} ')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left--{self.arrows} ')


wizardo = Wizard('Pawan', 50)
archero = Archer('Megha', 90)
wizardo.attack()
