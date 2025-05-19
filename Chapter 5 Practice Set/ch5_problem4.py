#What will be length of the following set

s = set()

s.add(20)
s.add(20.0) #in python if values are same numerically it will count as equal 20 == 20.0
s.add("20")

print(len(s)) #3