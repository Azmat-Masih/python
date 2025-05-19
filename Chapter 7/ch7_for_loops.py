# For Loops

# Range(start,stop,step_sizing)

# Printing number 0 to 5
for i in range(6):
    print(i)

# Printing numbers 0 to 50
for i in range(51):
    print(i)

# Printing the names of the list using for loops
names_list = ["harry", "jake", "peter", "Lux", "Sam", "Elon", 1, 5, 6, 7, 8, 9]
for i in range(len(names_list)):
    print(names_list[i])


# Step sizing
for i in range(0,100,5): #set sizing # first 0 to 100 and then 0 to 5 add
    print(i)


# printing list using for loop
list_ = ["harry", "jake", "peter", "Lux", "Sam", "Elon", 1, 5, 6, 7, 8, 9]
for i in list_:
    print(i)

# printing tuple using for loop
tuple_ = (1,4,6,7,2,5,8)
for i in tuple_:
    print(i)

# printing string using for loop
my_name = "Elon Musk"
for i in my_name:
    print(i)


# For loop with else
items = ["orange", "banana","apple","grapes"]
for i in items:
    print(i)
else: # runs after the loop is complete # mostly not used in industry
    print("this loop is done !")