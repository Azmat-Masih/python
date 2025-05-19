'''
Chapter 11 Inheritence and more on OOPs
'''

class Employee: #Base class / Parent Class
    company = "ABC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salaray}")



'''
This method is lenthy if we copy and paste the code, there will be chance of error.
'''
# class Programmer:
#     company = "ABC Tech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salaray}")
    
#     def showLanguage(self):
#         print(f"The name is {self.name} and the salary is {self.salaray}")




'''
So, we inherit the methods of employee using this
'''
class Programmer(Employee):
    company = "ABC Tech"
    def showLange(self):
        print(f"This is the langauge method {self.name}")




a = Employee()
b = Programmer()

print(a.company, b.company)