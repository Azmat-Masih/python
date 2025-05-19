'''
Class Method:

When we use the self in the function 
it will call the instense attribute not 
the class attribute so in order to call 
the class attribute within the class we 
use class attribute.
'''

class Manager:
    a = 1

    @classmethod #Decorator#
    def show(cls):
        print(f"This is the value of a {cls.a}")


b = Manager()
b.a = 45


b.show()