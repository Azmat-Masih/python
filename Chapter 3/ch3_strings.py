# Different ways of assigning Strings
a = 'code' # single qoute
b = "with" # double qoute
c = ''' harry ''' # triple qoute


# Slicing in Strings
a = "CodeWithHarry"  #
print(a[0:1]) #output C

print(a[0:5]) #output CodeW

b = "IamProudOfMyself"
print(b[0:]) #IamProudOfMysel
print(b[0]) #I
print(b[4:6]) #ro
print(b[:8]) #IamProud

# Negative Slicing
c = "JakeDaniel" 
#   -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
print(c[-1]) # l
print(c[-1:]) # l
print(c[:-1]) # JakeDanie
print(c[-4:-2]) # ni

# Slicing Skip Value
d = "IamGoingToDubaiThisYear"
print("this is skip slicing: ",d[0:4:2]) #Im
print("this is skip slicing: ",d[0:9:3]) # [0:9] IamGoingT, [0:3] Gn #Final output IGn
print("this is skip slicing: ",d[3:13:2]) # [3:13] GoingToDub , [3:2] itu #Final output Gigou
print("this is skip slicing: ",d[1:16:5]) # [1:16] amGoingToDubaiT , [1:5] nu #Final output anu