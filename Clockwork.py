#****************************************************************************
#Programmer 1: Geff Freire (ZeroRX)/ZERO aka GreatLeaderTechnus             *
#Programmer 2: Matt (MountainDreamin)                                       *
#Date: November 09, 2024                                                    *
#Program: Clockwork                                                         *
#Purpose: Logic Control System for Phonedle (SCC Hacks 2024)                *
#Inputs: Numerical Outputs from MountainDreamin's Dictionary Log Programming*
#****************************************************************************
class Clockwork: 

#Create a Dictionary to hold values of
    def __init__(self, name, phonNum):
        self.name = name
        self.phonNum = phonNum

#Build the dictionary of the phone number and names
    def BuildNum (name, phonNum):
        Contact = {phonNum:name}
# "Check if the key is of integer datatype. Next, during iteration, type cast it into a string then index it and check the "
        for num in Contact.getKey():
             

