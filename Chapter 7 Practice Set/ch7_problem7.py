#Write a program to create thr following star pattren

#   *
#  ***
# *****

# for n = 3

num1 = int(input("write number here: "))

for i in range(1, num1 + 1):
    print(" " * (num1 - i), end="")
    print("*" * (2*i-1), end="")
    print("")