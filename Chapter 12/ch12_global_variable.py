'''
Global Variable
'''

a =  89

def num():
    global a
    a = 3
    print(a)

num()
print(a)