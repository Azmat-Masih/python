# Write a python program which converts inches into cm


def coverts_inches_into_cms(inches):
    return inches * 2.54 #formula for converting inches into centimeter
    


user_input = int(input("write inches here: "))
centimeter = coverts_inches_into_cms(user_input)

print(f"{user_input} inches to centimeter {centimeter}")