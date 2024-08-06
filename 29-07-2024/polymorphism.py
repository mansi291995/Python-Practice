#poly means many morphism means many forms
#depending on data it will take many forms.
#method overridding
# class teacher:
#     def learn(self):
#         print("from teacher class")

# class student:
#     def learn(self):
#         print("from student class")

# obj1=teacher()
# obj2=student()
# obj1.learn()
# obj2.learn()
#method overloading 
#same function name different argument
class animal1:
    def animal(self,name,age):
        print(name,age)
    def animal(self,name):
        print(name)
    def animal(self,name=" ",bread=""):
        print(name,bread)
ane=animal1()
ane.animal("dog","pug")
ane.animal("cat",34)
ane.animal("bunny")
# class Student:
#     def student(self):
#         print("Welcome to azad class")
#     def student(self, name):
#          print("Welcome to azad class", name)
#     def student(self, name = "", course = ""):
#          print("Welcome to azad class", name, course)
# stud = Student()
# stud.student()
# stud.student("Ajay")
# stud.student("Ajay", "DS")