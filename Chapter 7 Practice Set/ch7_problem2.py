#Write a program to greet the names stored in list. Starting with S

name_list = ["harry","azmat","sam","jake","shaira","salman"]

for i in name_list:
    if(i.startswith("s")):
        print("hellow", i)
    else:
        print(i)