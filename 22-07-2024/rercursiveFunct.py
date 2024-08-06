def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

n = 5
print(f"Fibonacci number at position {n} is {fibonacci(n)}")
for i in range(10):
    print(i)
