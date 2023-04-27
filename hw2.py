class Bank:
    def __init__(self, name, head_name, coef):
        self.name = name
        self.head_name = head_name
        self.__coef = coef
    
    @property
    def coef(self):
        return self.__coef
    
    @coef.setter
    def coef(self, value):
        if 0.0 <= value <= 100.0:
            self.__coef = value
        else:
            raise ValueError("The coefficient must be between 0.0 and 100.0")
    
    def calculate(self, client, n):
        return client.money * (1 + self.coef/100) ** n

class Client:
    def __init__(self, name, id, bank, money):
        self.name = name
        self.id = id
        self.bank = bank
        self.__money = money
        self.__money_after_year = None
    
    @property
    def money(self):
        return self.__money
    
    @property
    def money_after_year(self):
        if self.__money_after_year is None:
            self.__money_after_year = self.bank.calculate(self, 1)
        return self.__money_after_year
    
    def invest(self, amount):
        if amount > 0:
            self.__money += amount
        else:
            print("The amount should be positive")
    
    def take_money(self, amount):
        if amount > 0:
            if self.__money >= amount:
                self.__money -= amount
            else:
                print("Not enough money")
        else:
            print("The amount should be positive")
