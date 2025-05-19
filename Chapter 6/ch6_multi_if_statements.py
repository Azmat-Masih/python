# What if there are multi if statements used

# We can use as much as elif in our conditions
# Last else will only be exute if all the elif condition are not met

u_inp = int(input("enter age: "))

# first if
if(u_inp > 50):
    print("you are above 50 years.")

# second if
if(u_inp == 50):
    print("you are 50 years old.")

# third if
if(u_inp >= 18):
    print("you are eligible for this.")
elif(u_inp == 0):
    print("enter correct age.")
elif(u_inp < 0):
    print("you are enter age in negative. which is not realistic.")
else:
    print("you are not eligible.")