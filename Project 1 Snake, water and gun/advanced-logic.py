''' 

    if(computer_input == -1 and your_value ==1): -1 - 1 = -2
        print("You Win !")
    elif(computer_input == -1 and your_value == 0 ): -1 - 0 = -1
        print("You Lose !")
    elif(computer_input == 1 and your_value == -1 ):  1 - (-1) = 2
        print("You Lose !")
    elif(computer_input == 1 and your_value ==  0 ): 1 - 0 = 1
        print("You Win !")
    elif(computer_input == 0 and your_value == -1 ): 0 - (-1) = 1
        print("You Win !")
    elif(computer_input == 0 and your_value == 1 ): 0 - 1 = -1
        print("You Lose !")
    else:
        print("Something went Wrong ! ")
        
'''

if ((computer_input - your_value) == -1 or (computer_input - your_value) == 2):
    print("You Win !")
else:
    print("You ")