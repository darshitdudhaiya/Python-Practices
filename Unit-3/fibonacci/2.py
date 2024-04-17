# 1 1 2 3 5 8

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter number : "))

print(f"fib({n}) = {fib(n)}")

