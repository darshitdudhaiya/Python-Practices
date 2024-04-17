class Person:
    def __init__(self, name="", age=0, address="", email="", contact=""):
        print("Constructor Is Called")
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        self.contact = contact

    def __del__(self):
        print("Destructor Is Called")

    def __str__(self):
        return f"""
            Name    : {self.name}
            Age     : {self.age}
            Address : {self.address}
            Email   : {self.email}
            Contact : {self.contact}
        """

p1 = Person("Steve", address="LA", email="steve@steve.steve", contact="+1-21345678910")
print(p1)