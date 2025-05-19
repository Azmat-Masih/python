def name():
    print("This is my name: ")
    
# name()

# print(__name__)

if(__name__ == "__main__"):
    # Following code will excutes. if the this codes executes in the same file.
    print("This code is directly excute from this file. ")
    name()
    print(__name__)