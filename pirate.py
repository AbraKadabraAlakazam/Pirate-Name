import random
from tkinter import *

class PirateNameGenerator:

    # Properties
    origFirst = ""
    origLast = ""

    # Properties - lists of names
    firstList = ["Captain", "Peg Leg", "Dead Man", "Scallywag"]
    lastList = ["O' Fish", "Of Dark Water", "Sea Wolf", "Ned Hed"]

    # Methods
    def __init__(self, firstName, lastName):
        self.origFirst = firstName
        self.origLast = lastName

    def CreateName(self):
        x = random.randint(0, len(self.firstList)-1)
        y = random.randint(0, len(self.lastList)-1)
        return self.firstList[x] + " " + self.lastList[y]

def buttonClick():
    # Get info out of the boxes
    first = fText.get()
    last = lText.get()
    # Create an instance of our generator
    mygen= PirateNameGenerator(first, last)
    # Run the generator
    pName = mygen.CreateName()
    # Show it on the screen
    output.config(text =pName, image=banner, compound= CENTER)
#mypirate = PirateNameGenerator("Umar", "Sheikh")
#print(mypirate.CreateName())


root = Tk()
# Customizable Variables
ft="Arial 14"
bg1="white"
fg1="Orange"
# Register the image
banner = PhotoImage(file="banner1.gif")
# Create Controls
title  = Label(root, text="What is your Pirate Name?", font = "Impact 20 bold", bg=bg1, fg=fg1)
fLabel = Label(root, text= "First Name", font = ft, fg= fg1, bg=bg1)
fText = Entry (root, font = ft, fg = fg1, bg= bg1)
lLabel = Label(root, text= "Last Name", font = ft, fg= fg1, bg=bg1)
lText = Entry (root, font = ft, fg = fg1, bg= bg1)
btn = Button(root, font =ft, fg=fg1, bg=bg1, text="Show me my name!", command =buttonClick)
output= Label(root, image=banner, font="Gabriola 20 bold")

# Add them to the screen
title.grid(row=0, column=0, columnspan=2)
fText.grid(row=1, column=1)
fLabel.grid(row=1, column=0)
lText.grid(row=2, column=1)
lLabel.grid(row=2, column=0)
btn.grid(row=3, column = 0, columnspan=2)
output.grid(row=4, column=0, columnspan=2)
# End
root.mainloop()




