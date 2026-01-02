class Parent_class:
    def __init__(self,name,age):
       self.name = name
       self.age = age 
    def description(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Parent_class):
    def __init__(self,name, age, deg):
        self.deg = deg
        super().__init__(name, age)
    def student_des(self):
        print(f"Name: {self.name}, Age:{self.age}, Deg: {self.deg}")
    

rohim = Student('Rohim', 20, "BSc" )
rohim.description()
rohim.student_des()
        