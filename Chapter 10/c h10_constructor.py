'''
Static Method 

Stateic method jisy object ki zarorat nh h.

'''



class Employee_data:
    name = "Jake"
    age = 15
    gender = "male"


    def __init__(self): #Dundur method which is autometically call. # Sepeical method  # Constructor #
       print("I m creating an object")


    def get_info(self):# This is method #  #If we don't use "self" we will see error. We can name self with other name, Self is just dicripited word.
        print(f"Name is {self.name}, Age is {self.age}, Gender is {self.gender}.")

    @staticmethod #we use staticmethod for not passing whole object in the method   # staticmethod ak decorator hota hai.
    def greet():
        print("Hello g this is greeting.")



jan = Employee_data()
jan.name = "Peter Macklin"
jan.get_info()
jan.greet()

