from abc import ABC, abstractmethod
class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1
    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print(f"{self.name} атакует мечом!")

class Mage(Hero):
    def attack(self):
        print(f"{self.name} использует магию!")

class Assassin(Hero):
    def attack(self):
        print(f"{self.name} атакует из-под тишка!")
warrior = Warrior("Кирито", 15, 120, 20)
mage = Mage("Лифа", 12, 85, 19)
assassin = Assassin("Рон", 9, 100, 17)

warrior.greet()
warrior.attack()
warrior.rest()
print()
mage.greet()
mage.attack()
mage.rest()
print()
assassin.greet()
assassin.attack()
assassin.rest()