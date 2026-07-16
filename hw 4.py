class Money:
    rates = {
        "KGS": 1,
        "USD": 89,
        "EUR": 96,
        "RUB": 1.2
    }
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    def convert_to_kgs(self):
        return self.amount * self.rates[self.currency]
    def __add__(self, other):
        return self.convert_to_kgs()+other.convert_to_kgs()
    def __mul__(self, other):
        return  self.convert_to_kgs()*other.convert_to_kgs()
    def __truediv__(self, other):
        return self.convert_to_kgs()/other.convert_to_kgs()
    def __str__(self):
        return f"{self.amount} {self.currency}"

mny1 = Money(43, "EUR")
mny2 = Money(8765, "USD")
print(mny1 + mny2)
print(mny1 * mny2)
print(mny1 / mny2)
print(mny1)