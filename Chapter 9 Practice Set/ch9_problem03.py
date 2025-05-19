'''
Write a program to generate multiplication tables from  2 to 20 and write it to the different file. 
Place these file in folder for a 13-year old.

'''

# Creating Function for generating tables and writing them in the folder #
def gen_table(n):
    table = ""
    for i in range(1,11):
        table += f"{n} x {i} = {n * i}\n"
        with open(f"tables/table_{n}", "w") as f:
            f.write(table)





# Creating loop
for i in range(2,21):
    gen_table(i)