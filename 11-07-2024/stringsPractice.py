# char='A'
# print(ord(char))
# print(chr(65))
# striing ="    mansi ekbote     "
# print(striing[::-1])
# print(striing[1])
# print(len(striing))
# c=striing.strip()
# print(len(c))

# #iterating string
# a="abcdefghijklmnopqrstuvwxyz"
# for i in striing:
#     print([i])
# template = "Hello, {} Welcome to {}"
# a="Bijay"
# b="Data Science"
# message = template.format(a,b)
# print(message)
list1=[1,2,3]
list2=[1,3,4]
res=[]
for i in list1:
    for j in list2:
        print(i,j)       
print([i for i in list1 ])
print(len(list1))
a=len(list1)
c=len(list2)
print(f"the length of list2 is {a}")
print(f"the length of list2 is {c}")
# if a<=c:
#     print("both are same")
# else:
#     print("different")
for i in list1:
    for j in list2:
        if(list1[i]==list2[j]):
            True
        else:
           False
if True:
    print("index are eqaual")
else:
    print("not equal")