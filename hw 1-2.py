class Hero:
    def __init__(self, name, level, health, strength):
        self.hero_name = name
        self.hero_level = level
        self.hero_health = health
        self.hero_strength = strength
    def greet(self):
        return f'\tПривет, я {self.hero_name},\n мой уровень-{self.hero_level}\n мое здоровье-{self.hero_health}\n моя сила-{self.hero_strength}'
    def attack(self):
        self.hero_strength -=1
        return f'\t{self.hero_name} наносит удар!\n герой устал, осталось {self.hero_strength} сил'
    def rest(self):
        self.hero_health += 10
        return f'\t{self.hero_name} вылечился!\n здоровье {self.hero_health} '



colt = Hero('Colt', 12, 100, 20)
shelly = Hero('Shelly', 10, 110, 15)
print(colt.greet())
print(colt.attack())
print(colt.rest())
print(shelly.greet())
print(shelly.attack())
print(shelly.rest())
