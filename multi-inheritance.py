class Car:
    def __init__(self,name):
        self.name = name

class Engine(Car):
    def details(self,engine_name):
     self.engine_name = engine_name
     print(f"{self.name} engine Start with the {self.engine_name}")
class MusicStyle(Car):
    def music(self):
        print(f"{self.name} car start the music after {self.name}")
      
   


class Car_category(MusicStyle,Engine):
    pass

toyota = Car_category("Toyota", )
toyota.details("Hybrid")
toyota.music()
