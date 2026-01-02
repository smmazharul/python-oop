
class Student:
    count = 0
    passing_year = 2025
    def __init__(self,name,age,roll):
        self.name = name 
        self.age = age
        self.roll = roll
        Student.count += 1

student1 = Student("Mazharul", 25, 15)
student2 = Student("Shuvo", 27, 2)
student3 = Student("Raju", 25, 8)
student1.passing_year = 2016
print(student1.name, student1.age, student1.roll, student1.passing_year)

print(Student.count)

        