class Hero:
    def __init__(self, name, lvl, hp):
         self.name = name
         self.lvl = lvl
         self.hp = hp
    def action(self):
         print(f'{self.name} готов к бою!')
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    def action(self):
        print(f'Маг {self.name} кастует заклинание! MP: {self.mp}')
class WarriorHero(Hero):
    def __init__(self, name, lvl, hp):
        super().__init__(name, lvl, hp)
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")

class BankAccount:
    bank_name = 'hero bank'
    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password
    def login(self, password):
        if password == self.__password:
            return True
        else:
            return False
    @property
    def full_info(self):
        return f'Герой: {self.hero.name}, Баланс: {self._balance}'
    def get_bank_name(self):
        print(self.bank_name)
    def bonus_for_level(self):
        if self.hero.lvl >= 10:
                self._balance += 10
        else:
            pass
    def __str__(self):
        return f'{self.hero}| Баланс: {self._balance}'
    def __add__(self, other):
        if type(other.hero) == type(self.hero):
            return self._balance + other._balance
        else:
            pass
    def __eq__(self, other):
        return (
                type(self.hero) == type(other.hero)
                and self.hero.lvl == other.hero.lvl
        )


ee = BankAccount(Hero, 10, "ljhg")

print(ee.full_info)





