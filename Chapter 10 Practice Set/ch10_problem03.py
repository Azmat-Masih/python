'''
Create a class with a class attribute a: create an object from it and set 'a'
directly using object.a = o. Does this change the class attribute ?
'''

class Demo:
    a = 4

o = Demo() #creating Object
print(o.a) #will print class attribute because right now we don't have instance attribute.

o.a = "0"
print(o.a) #Now it will change the value to 0 because we have not instance attribute
