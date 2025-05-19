# File I/O input and output

# Modes
'''

r = open for reading
w = open for writing
a = open for appending
+ = open for updating
rb = wil open for read in binary mode
rt = will open for read in text mode


with-statement = The best way to open and close the file is with statement



'''

# For write the data in thistext.txt #
# f = open("thistext.txt","w")
# f.write("Hello this is my first program using I/O.")
# f.close()

# For read the data in thistext.txt #
# f = open("thistext.txt","r")
# print(f.read())
# f.close()

# For Appending the text in thistext.txt #
# f = open("thistext.txt", "a")
# f.write(" This is second line which is appended.")
# f.close()

# For updating the text in thistext.txt #
# f = open("thistext.txt", "w+")
# f.write("This is the updating text. ")
# f.close()


# For binary mode the text in thistext.txt #
f = open("thistext.txt","rb")
print(f.read())
f.close()



 