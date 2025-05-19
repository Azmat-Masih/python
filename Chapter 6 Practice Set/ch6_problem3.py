# A spam comment as defined a text containing following keywords
# Make a lot of money #Buy now, #Subscribe this, #Click this. Write a program to detect this spams

p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "Click this"

user_msg = input("write your msg here: ")

if((user_msg in p1) or (user_msg in p2) or (user_msg in p3) or (user_msg in p4)):
    print("This is a spam comment")
else:
    print("This is important msg. ")