#Write a program to accepts marks of 6 students and display them in a sorted manner


student_marks_list = []

s1 = int(input("Write students marks here: "))
student_marks_list.append(s1)

s2 = int(input("Write students marks here: "))
student_marks_list.append(s2)

s3 = int(input("Write students marks here: "))
student_marks_list.append(s3)

s4 = int(input("Write students marks here: "))
student_marks_list.append(s4)

s5 = int(input("Write students marks here: "))
student_marks_list.append(s5)

s6 = int(input("Write students marks here: "))
student_marks_list.append(s6)


student_marks_list.sort()
print(student_marks_list)