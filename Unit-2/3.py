class Person:
    def __init__(self):
        print("Constructor Is Called")
        self.name = ""
        self.age = 0
        self.address = ""
        self.email = ""
        self.contact = ""

    def __del__(self):
        print("Destructor Is Called")

    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
    def setAddress(self, address):
        self.address = address
    def setEmail(self, email):
        self.email = email
    def setContact(self, contact):
        self.contact = contact

    def __str__(self):
        return f"""
            Name    : {self.name}
            Age     : {self.age}
            Address : {self.address}
            Email   : {self.email}
            Contact : {self.contact}
        """

p1 = Person()
print("Object Is Created")
p1.setName("Steve")
p1.setAge(40)
p1.setAddress("LA")
p1.setEmail("steve01@gmail.com")
p1.setContact("+1 - 6556988945")
print(p1)