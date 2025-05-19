'''
We use finally in functions, 
sometimes we need to show/print/excute 
something after the try or exception case, so we use finally.

Even a functions returns, finally excute at the end.

'''

def main():
    try:
        a = int(input("Enter the number: "))
        return
    
    except Exception as e:
        print(e)
        return
    
    finally: #This will run dosen't matter try runs or exceptions runs
        print("This is inside the finally block.")
        

main()
        