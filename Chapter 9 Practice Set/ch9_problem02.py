'''
The game() function in program lets a user play a game and returns the score as an integer. 
You need to read a file "hi-score.txt" which is either blank or contains the 
previous Hi-score. You need to write a program to update the hi-score whenever the game() 
function breaks the Hi-score.

'''

import random

def game():
    print("You are playing the game.")
    score = random.randint(1,50)
    
    # Reading the data from the file
    with open("score.txt","r") as f:
        hi_score = f.read()
        if(hi_score != ""):
            hi_score = int(hi_score)
        else:
            hi_score = 0

    

    print(f"Your Score: {score}")
    if(score > hi_score):
        # Writing the file data
        with open("score.txt","w") as f:
            f.write(str(score))

    
    return score

game()