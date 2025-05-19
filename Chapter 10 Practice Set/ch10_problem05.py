'''
Write a class train which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under indian railways.

'''
import random

class Train:

    def __init__(self, trainNum):
        self.trainNum = trainNum

    
    def book(self, fro, to):
        print(f"Ticket is booked in {self.trainNum}, From {fro}, To {to}")

    def status(self):
        print(f"Train number: {self.trainNum}, is running on time.")

    def getFare(self, fro, to):
        print(f"Ticket fare in Train Number: {self.trainNum}. From {fro}, To {to} is {random.randint(3000,10000)}")
        


passenger = Train(2112343) #method
passenger.book("Karachi","Lahore")
passenger.status()
passenger.getFare("Karachi","Lahore")
