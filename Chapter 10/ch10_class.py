'''
Creating Class
'''


class Employee_data:
    name = "Punit"  
    age = 25        # Class Attribute
    salary = 10000000  # Class Attribute
    language = "Punjabi"  # Class Attribute


punit = Employee_data()
print(punit.name, punit.language, punit.age) 

jake = Employee_data()
jake.name = "Jake Daniel" # Object attribute
print(jake.name, jake.age, jake.language)

# Age, salary, Language are class attribute which are direct related to the class.