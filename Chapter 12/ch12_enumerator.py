
l = ["apple", "orrange,", "cake", "banana"]
index = 0
for item in l:
    print(f"At index{index}, {item}")
    index += 1
    
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)