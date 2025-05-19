'''
Can you change the self-parameter inside a class to something else (say "harry"). 
Try changing self to "slf" or "harry" and see the effects.

'''


import random

class Train:

    def __init__(slf, trainNum):
        slf.trainNum = trainNum

    
    def book(slf, fro, to):
        print(f"Ticket is booked in {slf.trainNum}, From {fro}, To {to}")

    def status(slf):
        print(f"Train number: {slf.trainNum}, is running on time.")

    def getFare(slf, fro, to):
        print(f"Ticket fare in Train Number: {slf.trainNum}. From {fro}, To {to} is {random.randint(3000,10000)}")
        


passenger = Train(2112343) #method
passenger.book("Karachi","Lahore")
passenger.status()
passenger.getFare("Karachi","Lahore")
