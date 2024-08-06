#map function

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x ** 2, numbers)

# print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
l1=[1,2,3,3]
a=map(lambda x: x*2,l1)
print(list(a))

#filter Function
l2=[1,2,3,4]
a=filter(lambda x:x%2==0,l2)
print(list(a))
l2=["book ","pen","pencil"]
b=filter(lambda x:"book" in  x ,l2)
print(list(b))