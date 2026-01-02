class Car:
    def __init__(self, name, color, mileage):
        self.name = name
        self.color = color
        self.__mileage = mileage
    def get_mileage(self):
        return self.__mileage
    def set_mileage(self,new_mileage):
        self.__mileage = new_mileage

BMW = Car("MBW", "black", 50)
BMW.name = "sdsdkhds"
BMW.set_mileage(20)
print(BMW.name)
print(BMW.get_mileage())



        
       