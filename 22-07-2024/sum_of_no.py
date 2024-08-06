# Ensure list1 is already defined
list1 = [0, 1, 8, 3, 4]

# Correctly iterating over the list
n=int(input("enter n value"))
for i in list1:
    print(i)
    if  n in list1:
        continue
    else:
        break
        