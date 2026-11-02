import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет! Я {self.name}.")

    def attack(self):
        print(f"{self.name} атакует!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает и восстанавливает здоровье.")
        print(f"Текущее здоровье: {self.health}")

class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina
    def attack(self):
        print("Воин атакует мечом!")

class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana
    def attack(self):
        print("Маг кастует заклинание!")

class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
    def attack(self):
        print("Ассасин атакует из-под тишка!")

warrior = Warrior("Воин", 5, 100, 20, 80)
mage = Mage("Маг", 5, 80, 25, 100)
assassin = Assassin("Ассасин", 5, 90, 22, 95)

heroes = { "Warrior": warrior,
    "Mage": mage,
    "Assassin": assassin}

print("=== Наши герои ===")

for hero in heroes.values():
    hero.greet()
    hero.attack()
    print()
wins = {
    "Warrior": "Assassin",
    "Assassin": "Mage",
    "Mage": "Warrior"}

print("Выберите героя: Warrior / Mage / Assassin")

choice = input("Ваш выбор: ").strip().capitalize()

if choice not in heroes:
    print("Ошибка! Такого героя нет.")

else:
    opponent_name = random.choice(list(heroes.keys()))

    print(f"Вы выбрали: {choice}")
    print(f"Противник: {opponent_name}")

    print("Бой начинается!")
    heroes[choice].attack()
    heroes[opponent_name].attack()

    if choice == opponent_name:
        print("Ничья!")

    elif wins[choice] == opponent_name:
        print(f"Вы победили! {choice} сильнее {opponent_name}!")

    else:
        print(f"{opponent_name} победил!")
