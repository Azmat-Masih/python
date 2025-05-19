#Write a program to find out the given number is prime or not

# A prime number is a natural number greater than 1 that has exactly two factors: 1 and itself.
# In other words, a prime number is only divisible by 1 and itself.

num_ = int(input("number here: "))

for i in range(2,num_):
    if(num_ % i) == 0:
        print("number is not prime")
        break
else:
    print("number is prime")