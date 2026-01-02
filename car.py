class Car:
    def __init__(self,name, year, color, is_stock):
        self.name = name
        self.year = year
        self.color = color
        self.is_stock = is_stock

    def details(self):
        print(f"Name: {self.name}, Color:{self.color}, Year:{self.year}, Stock:{self.is_stock}")