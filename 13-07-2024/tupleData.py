tupple=(1,2,3,"mansi",1,2,3,3)
print(tupple)

count_tuple=tupple.count(3)
print(f"the count of tuple is {count_tuple}")
print(tupple.index(1))
print([i for i,value  in enumerate(tupple)if value==3])
print(tupple)
tupple[0]=2
print(tupple)