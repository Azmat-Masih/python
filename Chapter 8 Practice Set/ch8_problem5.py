# Write a python function to print first n of the following partren 

# ***
# **
# *

# n = 3

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)



user_input = int(input("write number of stars here: "))
stars = pattern(user_input)
