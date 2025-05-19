'''
Self_Parameter

'''

class Employee_data:
    name = "Jake"
    age = 15
    gender = "male"

    def get_info(self):# This is method #  #If we don't use "self" we will see error. We can name self with other name, Self is just dicripited word.
        print(f"Name is {self.name}, Age is {self.age}, Gender is {self.gender}.")



jan = Employee_data()
jan.name = "Peter Macklin"
jan.get_info()
# jan.get_info(jan)
