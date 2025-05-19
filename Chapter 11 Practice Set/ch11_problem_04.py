'''
Write a class 'Complex' to represent complex numbers, 
along with overloaded operators '+' and '*' which adds and multiples them.

'''

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        # For (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}"


c1 = Complex(1,6)
c2 = Complex(3,7)

print(c1 + c2)