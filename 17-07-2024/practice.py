
def _func(n):
    n=int(input("enter value of n"))
    i=1
    fact=1
    while(i<=n):
        fact=fact*i
        i+=1
    print(f"the factorial of {n} is",fact)
def _sorting():
    list=[1,3,5,2,9]
    list.sort()
    print("printing sorted list")
    print(list)
def _userSort():
    list1=[]
    limit=int(input("Enter limit of list"))
    
    i=1
    while(i<=limit):
        n=int(input("Enter value of n"))
        list1.append(n)
        i+=1
    print(list1)
    # print("the length of list is ",len(list))
# _userSort()
# _func(9)
# _sorting()

