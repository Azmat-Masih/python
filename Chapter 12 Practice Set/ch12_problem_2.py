'''
Write a program to print third, fifth and seventh element from a list using function
'''

list_ = [1,2,3,4,5,6,7,8,9]

for index, item in enumerate(list_):
    if(index == 2 or index == 4 or index == 6):
        print(item)