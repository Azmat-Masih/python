'''
Write a python program to rename the file of "renamed_python.txt"

'''

with open("old.txt","r")as f:
    context = f.read()

with open("rename_python.txt","w")as f:
    f.write(context)
    