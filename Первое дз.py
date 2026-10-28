
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f'Привет, я {self.name}. Мой уровень {self.level}')

    def attack(self):
        print(self.name, 'атакует')
        self.strength -= 1

    def rest(self):
        print(self.name, 'отдыхает')
        self.health += 1


hero1= Hero('Макс', 5, 100, 20)
hero2 = Hero('Иван', 3, 80, 15)

hero1.greet()
print('Здоровье:', hero1.health)
print('Сила:', hero1.strength)
hero1.attack()
hero1.rest()
print('Здоровье после отдыха:', hero1.health)
print('Сила после атаки:', hero1.strength)

hero2.greet()
print('Здоровье:', hero2.health)
print('Сила:', hero2.strength)
hero2.attack()
hero2.rest()
print('Здоровье после отдыха:', hero2.health)
print('Сила после атаки:', hero2.strength)
