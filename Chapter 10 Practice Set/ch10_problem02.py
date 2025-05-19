'''
Write a class "Calculator" capable of finding square, cube and square root of a number.

'''

class Calculator():
    def __init__(self,n):
        self.n = n

    def squar(self):
        print(f"This is the square. {self.n * self.n}")

    def cube(self):
        print(f"This is the cube. {self.n * self.n * self.n}")

    def squar_root(self):
        print(f"This is the square root. {self.n ** 1/2}")


result = Calculator(6)
result.squar()
result.squar_root()
result.cube()