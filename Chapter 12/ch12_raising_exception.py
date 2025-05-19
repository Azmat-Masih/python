'''
Some times we need to crash the program, but we also need to the show error 
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey, Our program don't except the 0 number for division")

else:
    print(f"This is the divion of a / b {a/b}")
