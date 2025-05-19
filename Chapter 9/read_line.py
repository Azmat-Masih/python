
# Reading single lines #

f = open("file.txt")

# read_line1 = f.readline()
# print(read_line1,type(read_line1)) 

# read_line2 = f.readline()
# print(read_line2,type(read_line2)) 

# read_line3 = f.readline()
# print(read_line3,type(read_line3)) 


# Doing the above task using while loop #
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()


f.close()