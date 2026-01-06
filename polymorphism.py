class Drive:
    def power(self):
        pass

class TV(Drive):
    def power(self):
        print("TV ON ")

class Fan(Drive):
    def power(self):
        print("Fan ON ")
switch = [TV(),Fan()]
switch[1].power()