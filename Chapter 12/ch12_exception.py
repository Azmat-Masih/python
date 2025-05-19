'''
This will throw error and crash the program, if we enter strings 
'''
# a = int(input("Enter a number. "))
# print(a)

'''
For handling the above error, we will use try exception. This  will not show error or crash the program
It will run the other codes as well with out any error.
'''

# try:
#     a = int(input("Enter a number. "))
#     print(a)
    
# except Exception as e: #If no error, program will ignore this block.
#     print(e)
    
# print("Thank you.")



'''
For Specific error:
'''

try:
    a = int(input("Enter a number. "))
    print(a)
    
except ValueError as v:
    print("hello world.")
    print(v)

except ZeroDivisionError as z:
    print("this is zero division error")
    print(z)

except Exception as e: #If no error, program will ignore this block.
    print(e)
    


