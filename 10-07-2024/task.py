# movies=['meg','hulk','ironman','thor','gog',1,2,3] 
# # print(movies) 
# print(movies[1:7:-1])
# print([0]*10)
# print((0)*10)
# print([1,2,3]*10)
#print(list(range(1,8)*3))

# a=range(1,10,1)
# print(a)
# list=[1.0,4,7,0.0,1.4,6]
# print(sorted(list))
# list1=['a','i','h']
# print(sorted(list1))
book_name=["news","bhagvatGeeta","money can buy happiness"]

# print(sorted(book_name))
# print(book_name)
#print(book_name.remove("news"))
#print(book_name[1])
print(book_name)

print(book_name.index("news"))

print("news" in book_name) 
print("news" not in book_name)
book_name1=["news","bhagvatGeeta","money can buy happiness"]
book_name2=["hello","by","money can buy happiness"]
print("-------")
print(book_name1[-1] in book_name2)

book_name1.extend(book_name2)
print(book_name1)
book_name.clear()
print(book_name)
my_string = "Hello, World!"
print(my_string.split(','))