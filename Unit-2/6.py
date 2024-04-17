class A:
    def __init__(self):
        self.__x = "Hi"
        self.y = "bye"

    def display(self):
        print(f"__x = {self.__x}\ny= {self.y}")

o = A()
o.display()
# print(o.__x)