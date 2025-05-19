'''
Repeat the problem 4 for a list of such words censored 

'''

words = ["Donkey", "Bad", "ganda","Fuck"]

with open("bad_words.txt","r") as f:
    context = f.read()


# using for loop to replace every list word with hash #
for word in words:
    context = context.replace(word, "#" * len(word))

with open("bad_words.txt","w") as f:
    f.write(context)