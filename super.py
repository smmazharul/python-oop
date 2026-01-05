class Vehicle:
    def __init__(self,name):
        self.name= name 
        self.is_running = True

class Car(Vehicle):
    def __init__(self, name,color):
        super().__init__(name)
        self.color = color
    
my_car = Car("BMW", "Black")
print(my_car.name)
print(my_car.is_running)