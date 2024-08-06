#single inheritance
# a
# |
# |
# b
class a:
    def a1(self):
        print("a1 called")
class b(a):
    def b1(self):
        print("b1 called")
obj=b()
obj.a1()
obj.b1()

#multiple inheritance
#a    b
#\    /
# \  /
#   c

class mother:
    motherName=" manali"
    def mom(self):
        
        print(self.motherName)
class father:
    fatherName="manoj "
    def dad(self):
        
        print(self.fatherName)

class son(mother,father):
    def parents(self):
        print(f"introducing my mother {self.motherName} and father {self.fatherName}")

obj=son()
# obj.fatherName="Manoj"
# obj.motherName="Manali"
obj.parents()
obj.dad()
obj.mom()

print("-------------------------------------------------------------------------------------------")
#multilevel inehritance
#a
#|
#|
#b
#|
#|
#c
class grandparent:
    def __init__(self,grandfather):
        self.grandfather=grandfather
    def showgrandparent(self):
        print(f"my grandfather name is {self.grandfather}")
class parent(grandparent):
    def __init__(self, grandfather,parentname):
        super().__init__(grandfather)
        self.parentname=parentname
    
    def showparent(self):
        print(f"my parent name is {self.parentname}")
class child(parent):
    def __init__(self, grandfather, parentname,child):
        super().__init__(grandfather, parentname)
        self.child=child
    def showchild(self):
        print(f"i am child {self.child}")
        
child=child("purushottam","manoj","mansi")
child.showgrandparent()
child.showparent()
child.showchild()

print("----------------------------------------------------------------------------------------")
#hierarchical inheritance
#it has multipple derived classes
class a:
    def func1(self):
        print("func1")
class b(a):
    def func2(self):
       print("func2")
class c(a):
    def func3(self):
        print("func3")
obj1=c()
obj2=b()
obj1.func1()
obj1.func3()

obj2.func1()
obj2.func2()