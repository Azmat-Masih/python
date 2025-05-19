'''
list comprehension is an elegant way to create lists based on existing lists.

'''



# Normal Way #
myList = [1,3,5,6,7,8,9]

squareList = []

for item in myList:
    squareList.append(item * item)
    
print(squareList)


# Comprehensive Way #
list_ = [3,5,2,8,4,9]

new_List = [i * i for i in list_]
print(new_List)
