#Write a program to find out the given name is in the list or not.

user_name_list = ["tony", "harry", "bill", "parker"]

user_name = input("write your name here: ")

if(user_name in user_name_list):
    print("user name is in the list of invited members.")
else:
    print("User is not invited.")