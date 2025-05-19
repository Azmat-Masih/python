# Write a program using function to print the multplication of the given number


def table_function(num):
   
    # for i in range(1,11): #using for loop
    #     print(f"{num} x {i} = {num * i}")

    i = 1
    while(i < num ):
        print(f"{num} x {i} = {num * i}")
        i +=1



user_input = int(input("write number here: "))
table_function(user_input)
