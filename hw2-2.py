import random
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
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super(). __init__(name, level, health, strength)
        self.hero_stamina = stamina

    def attack(self):
        self.hero_strength -= 1
        return 'Воин атакует мечом!'
class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.hero_mana = mana
    def attack(self):
        self.hero_strength -= 1
        return 'Маг кастует заклинание!'
class Assasin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.hero_stealth = stealth
    def attack(self):
        self.hero_strength -=1
        return 'Ассасин атакует из-под тишка!'


askarWarrior = Warrior('Askar', 1, 10, 10, 50)
askarMage = Mage('Askar', 1, 10, 10, 50)
askarAssasin = Assasin('Askar', 1, 10, 10, 50)
print(askarAssasin.attack())
print(askarWarrior.attack())
print(askarMage.attack())
print(f'1) да\n2) нет')
heroes = [Warrior, Mage, Assasin]
try:
    minigame = int(input('хотели бы вы поиграть в мини игру? : '))
    if minigame == 1:
        print('1) Warrior')
        print('2) Mage')
        print('3) Assasin')
        brawler = input('выберите героя: ')
        if brawler == '1':
            print('вы выбрали Warrior')
        elif brawler == '2':
            print('вы выбрали Mage')
        elif brawler == '3':
            print('вы выбрали Assasin')
        enemy_hero = random.choice(heroes)
        print(f'противник: {enemy_hero.__name__}')
        if brawler == '1' and enemy_hero == Warrior or brawler =='2' and enemy_hero == Mage or brawler == '3' and enemy_hero == Assasin:
            print('Ничья!')
        elif brawler =='1' and enemy_hero == Assasin or brawler == '2' and enemy_hero == Warrior or brawler =='3' and enemy_hero == Mage:
            print('Ты победил!')
        elif brawler =='1' and enemy_hero == Mage or brawler =='2' and enemy_hero == Assasin or brawler == '3' and enemy_hero == Warrior:
            print('Ты проиграл...')
except:
    pass