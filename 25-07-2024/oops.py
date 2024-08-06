#what is class
class animal:
    #what is constructor
    #used intialize object of class
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info1(self):
        print(f"my dog nam e is{self.name}")
    def info2(self):
        print(f"my dog name is {self.name} and age is{self.age}")
obj1=animal("kito",3)
obj2=animal("monky",5)

#calling member function of class by instamce
obj1.info1()
obj2.info2()
