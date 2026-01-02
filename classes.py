# class Person:
#     def show_name(self,name):
#         print(f"My name is {name}")
# mazharul = Person()
# humayra = Person()
# humayra.show_name("Humayra")
# mazharul.show_name("Mazharul")


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def show_name(self):
        print(f"My name is {self.name} and I am cuurently {self.age}")
mazharul = Person("Mazharul",25)
mazharul.name = "Mazharul Islam bin Moksed Ali"
mazharul.show_name()
        


