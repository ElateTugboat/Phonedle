#****************************************************************************
#Programmer 1: Geff Freire (ZeroRX)/ZERO aka GreatLeaderTechnus             *
#Programmer 2: Matt (MountainDreamin)                                       *
#Date: November 09, 2024                                                    *
#Program: Clockwork                                                         *
#Purpose: Logic Control System for Phonedle (SCC Hacks 2024)                *
#Inputs: Numerical Outputs from MountainDreamin's Dictionary Log Programming*
#****************************************************************************
class Clockwork:
    contact1 = {"name":"Bill Johnson", "number":"8005882300"}

#Create a Dictionary to hold values of
    def __init__(self, name, phonNum):
        self.name = name
        self.phonNum = phonNum

#Build the dictionary of the phone number and names
    def BuildNum (name, phonNum):
        Contact = {name:phonNum}
        return Contact

    def LadiesDoIHazThisRight(Contact, Digi): #Reference: The Price is Right game "One Away" where contestants guessed car prices.
        for nums in Contact.getKey():
            CheckDigi= Contact.getKey(nums)
            if Digi == CheckDigi[nums]:
                print ("Digit is present in this number")
            #WHERE IS IT?! -BaleBat
                print ("Digit is present here", CheckDigi[nums])
    #Matt's Part:
    def boolPositions(contact, inputNum):
        userInput = str(inputNum)
        bools = list([])
        value = str(contact.value)
        var = 0
        while(var < len(userInput)):
            bools.append(userInput[var] == value[var])
            var += 1
        return bools

    def boolPositions(dict, name, inputNum):
        userInput = str(inputNum)
        bools = list([])
        value = str(dict[name])
        var = 0
        while(var < len(userInput)):
            bools.append(userInput[var] == value[var])
            var += 1
        return bools       

