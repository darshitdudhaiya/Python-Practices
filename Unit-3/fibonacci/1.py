# 1 1 2 3 5 8

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        a, b = 1,1
        for x in range(3, n + 1):
            a, b = b, a + b
        return b

n = int(input("Enter number : "))

print(f"fib({n}) = {fib(n)}")

