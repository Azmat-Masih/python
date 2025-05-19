'''
Operator Overloading:

In python everything is class.
We can use these types of operator to perform different operations.
'''

class Neon:
    def __init__(self, n):
        self.n = n

    def __add__(self,num):
        return self.n + num.n



n = Neon(1)
m = Neon(4)

print(n + m)