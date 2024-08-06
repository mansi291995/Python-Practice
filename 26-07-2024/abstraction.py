from abc import ABC,abstractmethod
class car(ABC):
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year

    @abstractmethod
    def printDetails(self):
        pass
    def speed(self):
        print("speeding up")
class hatchback(car):
    def printDetails(self):
        print("name:",self.name)
        print("model",self.model)
        print("year",self.year)
car1=hatchback("Hyundai","i10",2022)
car1.printDetails()
car1.speed()
