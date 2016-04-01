import json
from random import randint

json_data = open('data.min.json')
parsed = json.load(json_data)

nameList = parsed['Age of Sigmar']


def splashScreen():
    print("|---+--- PATH TO GLORY ---+---|")
    print("    Which god do you serve?")
    print("\t1 - All of them")
    print("\t2 - Khorne")
    print("\t3 - Tzeentch")
    print("\t4 - Nurgle")
    print("\t5 - Slaanesh")


def rollDice():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    roll = str(d1) + str(d2)
    return roll


def generateFirst(roll):
    for entry in nameList:
        if roll == entry['roll']:
            return entry['first']


def generateSecond(roll):
    for entry in nameList:
        if roll == entry['roll']:
            return entry['second']


def genTitle(roll, god):
    for entry in nameList:
        if roll == entry['roll']:
            return entry['title'][god-1]


def createName(first, second, title):
    name = first + second + " " + title
    return name

splashScreen()
myGod = input("Please enter a number 1-5: ")

while myGod < 1 or myGod > 5:
    print("Enter a correct number, mortal!")
    myGod = input("Please enter a number 1-5: ")
    splashScreen()

firstName = generateFirst(rollDice())
secondName = generateSecond(rollDice())
title = genTitle(rollDice(), myGod)

fullName = createName(firstName, secondName, title)

print fullName
