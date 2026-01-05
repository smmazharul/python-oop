# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass

# class Car (Vehicle):
#     def start(self):
#         print("Car started")
#     def stop(self):
#         print("Car stoped")

# class Bike(Vehicle):
#     def start(self):
#         print("Bike started")
#     def stop(self):
#         print("Bike stoped")

# car = Car()
# bike = Bike()

# car.start()
# bike.stop()
# car.stop()
# bike.start()


#================== Shape Area Calculation===============

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Regtangle(Shape):
#     def area (self,length, width):
#         self.length= length
#         self.width = width
#         print(f"Area = {self.length * self.width}")


    
# r = Regtangle()
# r.area(2,3)

"""================== Bank System ==============="""

from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def interest_rate(self):
        pass

class BrackBank(Bank):
    def interest_rate(self):
        print("Interest Rate is 7 %")

b1 = BrackBank()
b1.interest_rate()
