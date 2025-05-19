'''
Create a class programm for storing information of few programmers working at microsoft

'''


class Programmers():
    company_name = "Microsoft"
    def __init__(self, name, salary, location):
        self.name = name
        self.salary = salary
        self.location = location


p = Programmers("Tony", 100000000, "karachi")
print(p.name, p.salary, p.location, p.company_name)

p = Programmers("Jacke Daniel", 600000000, "Lahore")
print(p.name, p.salary, p.location, p.company_name)