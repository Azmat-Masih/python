# f = open("thistext.txt","r")
# print(f.read())
# f.close()






# We can use with statement to automatically close the file #

with open("thistext.txt","r") as f:
    print(f.read())

# You don't have to explicity close the file #