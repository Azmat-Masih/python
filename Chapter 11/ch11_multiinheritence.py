class Employee:
    company = "Atlas.ai"
    name = "Default name"
    def show(self):
        print(f"This is the name of the company is {self.name}, {self.company} ")

class Coder:
    language_ = "Python"
    def language(self):
        print(f"This is the langauge of the programmer. {self.language_}")


class Programmer(Employee, Coder):
    company = "Omega Tech"
    def show_language(self):
        print(f"In company {self.company} This is the language is. {self.language_}")



a = Employee()
b = Programmer()

b.show()
b.language()
b.show_language()