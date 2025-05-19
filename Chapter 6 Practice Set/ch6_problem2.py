#write down a program to find out whether the student is passed. if it requires 40% atleast 33% in each subjects to pass.
# Assume 3 subjects and take the marks from user as input.

marks1 = int(input("enter marks 1: "))
marks2 = int(input("enter marks 1: "))
marks3 = int(input("enter marks 1: "))

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage >=40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("Wow. Your are Pass", total_percentage)
else:
    print("Sorry. You are fail.", total_percentage)