a={"name":"mansi","age":"56"}
b={"mansi":"name","56":"age"}
print(f"the girl name is :{a['name']}")
print(b)
list1 = (1, 2, 3)
list2 = ('a', 'b', 'c')
list3 = (True, False, True)
print("zipped area")
zipped = zip(list1, list2, list3)
print(type(zipped))
print(list(zipped))
stud=["mansi","yash","anjali"]
marks=["70","70","50"]
stud_marks={}
for stud,marks in zip(stud,marks):
    stud_marks[stud]=marks

print(stud_marks)
res=a.keys()
print(res)
print(a.values())
print(f"the name{a['name']}")
print("deep copy and shallow copy")
import copy
my_dict={"name":"mansi","attributes":{"age":25,"address":"pune"}}
new_dict=copy.deepcopy(my_dict)
print(new_dict)