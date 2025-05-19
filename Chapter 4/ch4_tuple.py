#Tuple in python are imuteble data type in python

a = () #empty tuple
print(type(a))

b = (1,) #sigle value tuple
print(type(b))

c = ( 3, 2, 5, True, "Tony") #multi value tuple
print(type(c))

# Methods in tuple
a = (1,2,3,1,324,43,5643,1,5425)
b = a.count(1) #gives the number of how many times 1 occurs in a 
print(b)
c = a.index(3) # gives the index of 3 occurs in a
print(c)

