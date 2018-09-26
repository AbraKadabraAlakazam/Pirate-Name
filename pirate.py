import random

class PirateNameGenerator:
    origFirst = ""
    origLast = ""

    firstList = ["Captain", "Peg Leg", "Dead Man", "Scallywag"]
    lastList = ["O' Fish", "Of Dark Water", "Sea Wolf", "Ned Hed"]

    def __init__(self, firstName, lastName):
        self.origFirst = firstName
        self.origLast = lastName

    def CreateName(self):
        x = random.randint(0, len(self.firstList)-1)
        y = random.randint(0, len(self.lastList)-1)
        return self.firstList[x] + " " + self.lastList[y]

mypirate = PirateNameGenerator("Umar", "Sheikh")
print(mypirate.CreateName())
