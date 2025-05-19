# Default parameter value

def greeting(name,greet="Good Morning"):
    print(f"{name}, {greet}")
    # print(greet)

greeting("tony") #If we don't pass the second parameter the default parameter which we set in fun def it will execute .
# greeting("harry","Good Afternoon") #If we pass the second parameter it will override the default parameter in fun def .









# Returning value in functions #  
def fun(name):
    avg = print("hellow, ",name)
    return avg
    # return 9 #For example purpose

a = fun("Tony")
print(a)