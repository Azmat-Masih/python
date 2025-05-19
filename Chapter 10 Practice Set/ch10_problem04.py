'''
Add a static method in problem 2, to greet the user with hello
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

    @staticmethod
    def greet():
        print("Hello g, Good morning.")


result = Calculator(6)
result.squar()
result.squar_root()
result.cube()
result.greet()