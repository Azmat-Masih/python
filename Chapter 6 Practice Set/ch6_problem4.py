#write a program to find the given username contains less then 10 characteres

username = input("write user name: ")
u_len = len(username)

print(u_len)

if(u_len < 10):
    print("user name contains less then 10 characters")
else:
    print("username contains more then 10 characters")