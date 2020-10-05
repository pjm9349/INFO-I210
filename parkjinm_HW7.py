#Justin Park
#INFO - I210

                                # Homework 7 #

# 9.20
from tkinter import*
import random

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()

        self.content = random.choice(range(10))
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text = "Enter your guess: ")
        self.lbl.grid()
        self.ent = Entry(self, width = 40)
        self.ent.grid()

        self.ent.bind("<Return>", self.guess2)
        self.bttn1 = Button(self, text = "Enter", command = self.guess)
        self.bttn1.grid()

    def guess(self):
        new_root = Tk()
        if self.ent.get() == str(self.content):
            self.content = random.choice(range(10))
            new_lbl = Label(new_root, text = "Let's do this again...", width = 40, height = 6)
            new_lbl.grid()
        else:
            new_lbl = Label(new_root, text = "Incorrect", width = 40, height = 6)
            new_lbl.grid()

    def guess2(self, guess):
        self.guess()

#Main
root = Tk()
root.title("tk")
root.geometry("410x220")

app = Application(root)

root.mainloop()

##Additional problem
from tkinter import*

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.lbl = Lable(self, text = "What would you like delivered? ")
        self.lbl.grid()
        self.ent = Entry(self, width = 30)
        self.ent.grid(row = 0, column = 1, sticky = W)
        self.lbl1 = Label(self, text = "Options")
        self.lbl1.grid(row = 1, column = 1, sticky = W)
        self.lbl2 = Label(self, text = "Delivery Method: ")
        self.lbl2.grid(row = 2, column = 0, sticky = W)
        self.lbl3 = Label(self, text = "Addons: ")
        self.lbl3.grid(row = 2, column = 1, sticky = W)

        self.addons = StringVar()
        self.addons.set("Self Driving Car($20)")

        Radiobutton(self, text = "Flying Drone($10)", variable = self.addons, value = "drone").grid(row = 3, column = 0, sticky = W)
