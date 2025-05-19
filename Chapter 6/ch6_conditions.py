# Condition Expressions

# Excuting instructions on conditions being met



a = False
if(a == True):
    print(" a is true ")
else:
    print("a is not true")


# if elif else lador

user_input = int(input("write your age: "))

if(user_input >= 18):
    print("your are egible for that.")
elif(user_input < 0):
    print("you enter the age in negative")
elif(user_input == 0):
    print("please enter correct age")
else:
    print("You are below the age. You are not eligible")

print("survey is done!")
