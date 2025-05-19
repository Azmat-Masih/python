'''
Write a program to mine a log file and find out whether it contains python.

'''

with open("log.txt","r") as f:
    context = f.read()
    if("Python" in context):
        print("Yes Python is the log.")
    else:
        print("User not Found")