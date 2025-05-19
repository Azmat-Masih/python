class Manager:
    a = 1

class Programmer(Manager):
    b = 2

class Coder(Programmer):
    c = 3


m = Manager
print(m.a)
# print(m.b) #Shows the error because b is not the attribute of manager

n = Programmer
print(n.a, n.b)

o = Coder
print(o.a, o.b, o.c)



