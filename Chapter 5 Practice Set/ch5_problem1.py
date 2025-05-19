# Wrtie a program to create a dictionary of hindi words with values as their english translation.
# Provide user with an option to look it up.

hindi_dic = {
    "madad" : "help",
    "kitab" : "book",
    "qalam" : "pen",
    "pani" : "water",
    "choha" : "rat",
}

user_input = input("Write here: ")

# hindi_dic.get(user_input)
# print(hindi_dic.get(user_input))
print(hindi_dic[user_input])