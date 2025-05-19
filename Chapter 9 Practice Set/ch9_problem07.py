'''
Do the same problem as problem 6, but now find in which line python exits

'''


with open("log.txt","r") as f:
    lines = f.readlines()

line_number = 1
for line in lines:
    if("Python" in line):
       print(f"Python exits: Python in line: {line_number}")
       break

    line_number += 1
    
else: 
    print("No Python exits")