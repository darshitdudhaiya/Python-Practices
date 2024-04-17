"""
    def <name of function>([<arguments>]):
        <code>
        [return <value>]
"""


def sayHello1():
    print("Hello!")

sayHello1()


def sayHello2(name):
    print(f"Hello {name}!")

sayHello2("Shaunak")

def sayHello3(name1, name2="Finch", name3="Steve"):
    print(f"Hello {name1}, {name2} and {name3}!")

# Steve, Finch and Shaunak
sayHello3(name1="Steve", name3="Shaunak")


def sum1(*nums):
    sum = 0
    for x in nums:
        sum += x
    return sum

print(sum1(5, 6, 7, 8, 9, 1.5, 10.11))

def demo(**kwargs):
    print(kwargs["name"])
    print(kwargs["course"])
    print(kwargs["semester"])
    print(kwargs["division"])

demo(name="Shaunak", course="BCA", semester=6, division="AB")
