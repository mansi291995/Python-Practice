def fact(n):
    
    if n==0:
        return 1
    
    return n * fact(n-1)

res=fact(4)
print(res)

def loap():
    i=0
    while(i<=10):
        i+=1
        print(i)
fact(3)