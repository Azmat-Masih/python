# Write a program using function to find the greatest of three numbers

def greatest_number():
    num1 = int(input("write number1 here: "))
    num2 = int(input("write number1 here: "))
    num3 = int(input("write number1 here: "))

    if(num1 > num2 and num1 > num3):
        print("number1 is the greatest number. ", num1)
    elif(num2 > num1 and num2 > num3):
        print("number2 is the greatest number. ", num2)
    elif(num3 > num1 and num3 > num2):
        print("number3 is the greatest number. ", num3)
    else:
        print("No number is greater")


greatest_number()