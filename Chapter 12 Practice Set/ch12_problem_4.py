'''
Write a program to display a/b where a and b are integers. If b = 0,
display infinite by handling the zeroDivisionError.

'''

# a = int(input("write first number here: "))
# b = int(input("write second number here: "))

try:
    a = int(input("write first number here: "))
    b = int(input("write second number here: "))
    print(f"a/b = {a/b}")

except ZeroDivisionError as v:
    print("Infinite Error")