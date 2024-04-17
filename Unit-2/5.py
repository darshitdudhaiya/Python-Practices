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

class Student(Person):
    def __init__(self, name="", age=0, address="", email="", contact="", course="", semester=1, division='A'):
        super().__init__(name, age, address, email, contact)
        # super().__init__()
        self.course = course
        self.semester = semester
        self.division = division

    def __str__(self):
        return f"""
            {super().__str__()}
            course   : {self.course}
            semster  : {self.semester}
            division : {self.division} 
        """

s1 = Student("Steve", 21, "LA", "steve@steve.steve", "+1-1234567890", "BCA", 6, 'A')
print(s1)
