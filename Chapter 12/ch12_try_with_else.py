'''
Try else
'''

try: #If try successful, else will run.
    a = int(input("Enter number: "))
    print(a)
    
except Exception as e:
    print(e)

else: #If everything goes correct else will run after try, if anything goes wrong the exceptions block will run.
    print("I m inside else. ")