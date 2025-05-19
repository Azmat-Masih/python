# Set in Python

#Set is a collection of well defined objects
# Value in set not repeat
# Set are unordered
# Set are un indexed
# Theres no way to change the value in sets
# Cannot contains duplicate value

empty_set = set() #Empty set syntex
print(type(empty_set)) 

set_1 = {1, 2, 3, 4, 5, 6, 7, 8} # Set cointaining value syntex
set_2 = {1, 4, 6, 8, 12, 56, 78}
print(type(set_1)) 

# Set methods


set_1.add(9) # adds 9 in set_1
print(set_1)

# Sets Operations
print(len(set_1)) #Gives the length of set_1

set_1.remove(6) #removes 6 from set_1 and update the set
print(set_1) 

set_2.pop() # removes any value value from set 
print(set_2)

# Union
print(set_1.union(set_2)) #Returns new set cointain value of both sets but not repeated
# Intersection
print(set_1.intersection(set_2)) #returns new set cointaining same value in both sets

set_1.clear() #Empty the sets
print(set_1)