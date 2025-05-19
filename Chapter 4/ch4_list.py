#List in Python are muteable (means they can change)

#List in python stores different types of data types in it
a = ["jake", 1, 0.45345, True, "peter", 342]

a.append("Working") #adds working in the end of the index
print(a)

b = [1 , 3, 9, 2, 65, 7, 4, 82]
b.sort() # arrange the list in order
print(b)

c = [2, 5, 7, 4, 2, 4, 6, 9]
c.reverse() # arrange the list in reverse order
print(c)

d = ["orange", "apple", "banana", "cake", "charry"]
d.insert(3,"Grapes") #insert grapes at index  3
print(d)

e = ["orange", "apple", "banana", "cake", "charry"]
print(e.pop(3)) # will delete element at the given index and return the value
print(e)

f = [2, 5, 7, 4, 2, 4, 6, 9]
f.remove(7) # remove the given value from the index
print(f)