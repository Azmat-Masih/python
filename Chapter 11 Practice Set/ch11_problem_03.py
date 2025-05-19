'''
Create a class 'Employee' and add salary and increment properties to it.

Write a method 'Salary afterIncrement' method with a @property decorator with a setter
which change the value of increment based on the salary.
'''

class Employee:
    salary = 6543
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary / self.salary) -1 ) * 100

e = Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 90343
print(e.increment)