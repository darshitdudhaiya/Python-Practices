def higherOrderFunction(foo, a):
    foo(a)

higherOrderFunction(print, "Hello")

def print2():
    return print

print2()("Hi")

print3 = print2()

print3("How are you?")
