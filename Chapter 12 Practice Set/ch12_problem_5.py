'''
Store the multiplication tables generated in problem 3 in a file named tables.txt
'''

n = int(input("Write number here: "))

table = [n*i for i in range(1,11)]
with open("tables.txt","a") as f:
    f.write(str(table) + "\n")