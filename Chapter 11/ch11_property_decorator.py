'''
Property Decorator:



'''

class Employee:
    a = 1
    def show(self):
        print(f"This is the value of a: {self.a}")

    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

m = Employee()

m.name = "Bill Gates"
print(m.fname, m.lname)