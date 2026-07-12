from abc import ABC, abstractmethod
class Hero(ABC):
    @abstractmethod
    def attack(self):
        pass
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength
    def greet(self):
        return f'Привет, меня зовут {self.name}, мой уровень {self.level}'
    def rest(self):
        self.__health += 1
        return f'{self.name} отдыхает'
class Warrior(Hero):
    def attack(self):
        return 'Воин атакует мечом!'
class Mage(Hero):
    def attack(self):
        return'Маг использует магию'
class Assassin(Hero):
    def attack(self):
        return 'Ассасин атакует из-под тишка'
manW = Warrior('manW', 12,32,33)
manM = Mage('manM', 12,32,33)
manA = Assassin('manA', 22,432,32)
print(manW.greet())
print(manM.greet())
print(manA.greet())
print(manW.attack())
print(manM.attack())
print(manA.attack())
print(manW.rest())
print(manM.rest())

print(manA.rest())