# Write a program to calculate the factorial of the given numebr using for loop


num1 = int(input("write your numebr here to check the factorial: "))

f_ = 1

for i in range(1, num1+1):
    f_ = f_ *  i

print(f"Factorial of {num1} is {f_}")