from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car (Vehicle):
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stoped")

class Bike(Vehicle):
    def start(self):
        print("Bike started")
    def stop(self):
        print("Bike stoped")

car = Car()
bike = Bike()

car.start()
bike.stop()
car.stop()
bike.start()
