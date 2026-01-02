class Car:
    def __init__(self,name,color,mileage):
        self.name = name 
        self.color = color
        self.__mileage = mileage
    def show_details(self):
        print(f"Name: {self.name}, Color: {self.color}, Mileage:{self.__mileage}")


BMW = Car("BMW", "Black", 50)
BMW.show_details()
        
       