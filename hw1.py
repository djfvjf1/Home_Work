from typing import List

class Holiday:
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    
    def __init__(self, name: str, day: int, month: str):
        self.name = name
        self.day = day
        self.month = month
    
    def __str__(self):
        return f"Happy {self.name} day!"
    
    def __eq__(self, other):
        return self.month == other.month
    
    def __lt__(self, other):
        return self.months.index(self.month) < self.months.index(other.month)
    
    def __le__(self, other):
        return self.months.index(self.month) <= self.months.index(other.month)
    
    def __gt__(self, other):
        return self.months.index(self.month) > self.months.index(other.month)
    
    def __ge__(self, other):
        return self.months.index(self.month) >= self.months.index(other.month)


class Employee:
    def __init__(self, name: str, salary: float, position: str):
        self.name = name
        self._salary = salary
        self.position = position
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        self._salary = value
    
    def __str__(self):
        return f"{self.name} at position {self.position}"

