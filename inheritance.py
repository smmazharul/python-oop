class Vehicle:
    def __init__(self, name):
        self.name = name
        self.is_running = True

class Car(Vehicle):
    def __init__(self, name, color):
        super().__init__(name)   
        self.color = color

class Bike(Vehicle):
    def door(self):
        print("Bike have no door")

BMW = Car("BMW", "black")

print(BMW.name)
print(BMW.is_running)
print(BMW.color)

honda =Bike("honda")
honda.door()
