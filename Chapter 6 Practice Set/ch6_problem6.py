#Write a progra mto calculate the marks of the student from the given scheme.

# 90 - 100 Ex
# 80 - 90 A
# 70 - 80 B
# 60 - 70 C
# 50 - 60 D
# < 50 F


user_marks = int(input("Write user marks here: "))

if(user_marks >=90):
    print("Excelent")
elif(user_marks >=80):
    print("A grade")
elif(user_marks >=70):
    print("B grade")
elif(user_marks >= 60):
    print("C Grade")
elif(user_marks >=50):
    print("D grade")
elif(user_marks < 50):
    print("You are fail try next time. ")