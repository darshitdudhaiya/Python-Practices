n = int(input("Enter No. : "))
# a = 0
# b = 1
# if n == 1:
#     print(a)
# elif n == 2:
#     print(f"{a} {b}")
# elif n <= 0:
#     print("Invalid input")
# else:
#     print(f"{a} {b}", end=" ")
#     for x in range(3, n + 1):
#         a, b = b, a + b
#         print(f"{b}", end=" ")

def fib(n):
    if n > 0:
        if n == 1:
            return 1
        else:
            if n >= 2:
                return fib(n - 1) + fib(n - 2)
    else:
        return

print(fib(5))

