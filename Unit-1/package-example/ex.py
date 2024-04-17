# import package1.calc1
# import package1.calc2
# import package1.* Not working
# from package1 import calc1, calc2
from package1.calc1 import *
from package1.calc2 import *

a = int(input("a : "))
b = int(input("b : "))

print(f"a + b = {add(a, b)}")
print(f"a X b = {mul(a, b)}")
print(f"a ^ b = {pow(a, b)}")
