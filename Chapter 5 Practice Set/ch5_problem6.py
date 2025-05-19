# Create a empty dictionary. 
# Ask your friend to add their favourite colors and use there names as key to color, 
# Assume names are unique

empty_dic = {}

friend1 = input("Write your name here: ")
friend1_f_c = input("Write your favourite color here: ")
empty_dic.update({friend1:friend1_f_c})

friend2 = input("Write your name here: ")
friend2_f_c = input("Write your favourite color here: ")
empty_dic.update({friend2:friend2_f_c})

friend3 = input("Write your name here: ")
friend3_f_c = input("Write your favourite color here: ")
empty_dic.update({friend3:friend3_f_c})

friend4 = input("Write your name here: ")
friend4_f_c = input("Write your favourite color here: ")
empty_dic.update({friend4:friend4_f_c})


print(empty_dic)