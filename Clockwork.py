#****************************************************************************
#Programmer 1: Geff Freire (ZeroRX)/ZERO aka GreatLeaderTechnus             *
#Programmer 2: Matt (MountainDreamin)                                       *
#Date: November 09, 2024                                                    *
#Program: Clockwork                                                         *
#Purpose: Logic Control System for Phonedle (SCC Hacks 2024)                *
#Inputs: Numerical Outputs from MountainDreamin's Dictionary Log Programming*
#****************************************************************************
class Clockwork():
    contact1 = {"name":"Bill Johnson", "number":8005882300}

#Create a Dictionary to hold values of
    def __init__(self, name, phonNum):
        self.name = name
        self.phonNum = phonNum

#Build the dictionary of the phone number and names
    def BuildNum (name, phonNum):
<<<<<<< HEAD
        Contact = name
        number = phonNum
=======
        Contact = {name:phonNum}
        return Contact

    def LadiesDoIHazThisRight(Contact, Digi): #Reference: The Price is Right game "One Away" where contestants guessed car prices.
        for nums in Contact.getKey():
            CheckDigi= Contact.getKey(nums)
            if Digi == CheckDigi[nums]:
                print ("Digit is present in this number")
            #WHERE IS IT?! -BaleBat
                print ("Digit is present here", CheckDigi[nums])
           

>>>>>>> 00c23b92a6659010dfeda2ce36defbfe1640c123
