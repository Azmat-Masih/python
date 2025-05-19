# Write a program to find the sum of first n natural numbers using while loops

num_ = int(input("Write number here: "))

i = 1
sum_ = 0

while(i <= num_):
    sum_ += i
    i += 1

print(sum_)