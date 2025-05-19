# Break statement in loops


for i in range(0,19):
    if(i == 15): #when the conditions is met the loop will end
        break
    print(i)

for i in range(0,20):
    if(i == 15): 
        continue #if the condition is met continue will skip that iteration and move to the next one
    print(i)


# Printing lists using break and continue statement
list_ = [1 , 2 ,3 ,4, 5, 6]
for i in list_:
    if(i == 3):
        break
    print(i)

name_list = ["harry", "jake", "peter", "Lux", "Sam", "Elon"]
for i in name_list:
    if(i == "Lux"):
        break
    print(i)

name_s = ["harry", "jake", "peter", "Lux", "Sam", "Elon"]
for i in name_s:
    if(i == "Sam"):
        continue
    print(i)