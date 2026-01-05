# class Vehicle:
#     def __init__(self,name):
#         self.name= name 
#         self.is_running = True

# class Car(Vehicle):
#     def __init__(self, name,color):
#         super().__init__(name)
#         self.color = color
    
# my_car = Car("BMW", "Black")
# print(my_car.name)
# print(my_car.is_running) 

"""==================Employee Salary System============"""

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary} ")

class Manager(Employee):
    def __init__(self, name, salary,bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def show_info(self):
        super().show_info()
        print(f"Bonus: {self.bonus}")
        print(f"Total Salary: {self.salary + self.bonus}")
m1 = Manager("Rahim",50000,10000)
m1.show_info()

