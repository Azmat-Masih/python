'''
Write a program to find out whether a file is identical and matches the content of another file.

'''


with open("bad_words.txt","r") as f:
    context1 = f.read()

with open("log.txt", "r") as f:
    context2 = f.read()

if(context1 == context2):
    print("yes both files data is identical.")
else:
    print("No identical, both files data is different.")