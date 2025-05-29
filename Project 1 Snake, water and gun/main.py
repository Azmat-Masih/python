'''

snake = 1
water = -1
gun   = 0

'''

import random #for random number 


game_dic = {"s": 1, "w": -1, "g": 0}
reversed_dic = {1: "snake", -1 : "water", 0 : "gun"}

computer_input = random.choice([0, 1, -1])
# print(computer_input)

your_input = input("what your input: ")
your_value = game_dic[your_input]

print(f'You chose {reversed_dic[your_value]},\nComputer chose {reversed_dic[computer_input]}')


if(computer_input == your_value):
    print("Game is draw !")
else:
    if(computer_input == -1 and your_value ==1):
        print("You Win !")
    elif(computer_input == -1 and your_value == 0 ):
        print("You Lose !")
    elif(computer_input == 1 and your_value == -1 ):
        print("You Lose !")
    elif(computer_input == 1 and your_value ==  0 ):
        print("You Win !")
    elif(computer_input == 0 and your_value == -1 ):
        print("You Win !")
    elif(computer_input == 0 and your_value == 1 ):
        print("You Lose !")
    else:
        print("Something went Wrong ! ")

