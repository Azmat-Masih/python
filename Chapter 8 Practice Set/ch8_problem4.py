# Write a recursive function to calculate the first n of natural numbers

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3 
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

'''



def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n



user_input = int(input("write number here: "))
total = sum(user_input)
print(total)