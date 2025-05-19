# Write a program to read the file name "poem.txt" and find that either this contains word "twinkle".


with open("poem.txt","r") as f:
    context = f.read()
    if("twinkle" in context):
        print("Yes is contains.")
    else:
        print("No it dosen't.")