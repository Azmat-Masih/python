'''
Some times we want to call two constructor of two objects at the same time, 
by default we can't call them together so we use super().__init() in class 
in which we call to the parent constructor of the class.
'''

class Manager:
    a = 1
    def __init__(self):
        print("This is manager constructor")

class Programmer(Manager):
    b = 2
    def __init__(self):
        print("This is programmer constructor")

class Coder(Programmer):
    c = 3
    def __init__(self):
        super().__init__() # This is super constructor
        print("This is coder constructor")


# m = Manager()
# print(m.a)
# print(m.b) 

# n = Programmer()
# print(n.a, n.b)

o = Coder()
print(o.a, o.b, o.c)



