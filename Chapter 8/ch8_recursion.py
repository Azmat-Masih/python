# Recursion
# Is a function which call itself

# Factorial 0 is bydefault 1

def fact(n):
    if(n==1 or n ==0):
        return 1
    return n * fact(n-1)


n = int(input("write number here: ")) #giving this n in the print
print(f"factorial of {n} is " , fact(n)) 