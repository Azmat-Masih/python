'''
Create a class (2-D Vector) and use it to create another class representing a 3-D vector.

'''

class twoDVector:
    def __init__(self, i, j):
        
        self.i = i
        self.j = j

    def show(self):
        print(f"This is the 2D-Vector {self.i}i + {self.j}j ")

    

class threeDVector(twoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)

        self.k = k

    def show(self):
        print(f"This is the 3D-Vector {self.i}i + {self.j}j + {self.k}k ")

a = twoDVector(1,5)
a.show()

b = threeDVector(1,6,2)
b.show()