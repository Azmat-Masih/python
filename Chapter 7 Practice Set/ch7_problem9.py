# Write a program to print the following start pattern


#  ***
#  * *
#  ***

num1 = int(input("write numebr here: "))
for i in range(1, num1-1):
    if(i == 1 or i == num1):
        print("*" * num1)
    else:
        print("*", end="")
        print(""*(2-1),end="")
        print("*", end="")
e