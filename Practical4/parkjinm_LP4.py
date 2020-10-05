# Justin Park
# INFO - I210
# Lab Practical 4

from tkinter import*
import random

class Application(Frame):

    # initializing the frame
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()


    # create widgets through starting with def fucntion, and put all the codes into there
    def create_widgets(self):
        Label(self, text = "Roman Numeral Canvas").grid(row=0, column=0, columnspan=6, sticky=S)
        Label(self, text = "Number:").grid(row=1, column=1)
        Label(self, text = "Line Width:").grid(row=2, column=1)
        Label(self, text = "Line Color:").grid(row=3, column=1)

        self.number=Entry(self)
        self.number.grid(row=1, column=2, columnspan=2)

        # Make the size of Canvas to 310 high and 500 wide
        self.canvas = Canvas(self, height = 310, width = 500)
        self.canvas.grid(row = 1, column = 0, rowspan = 4)

        # Create the radiobuttons for "Line Width:" 1,3, and 5
        self.width=StringVar()
        self.width.set("1")
        Radiobutton(self, text="1", variable=self.width, value="1").grid(row=2, column=2)
        Radiobutton(self, text="3", variable=self.width, value="3").grid(row=2, column=3)
        Radiobutton(self, text="5", variable=self.width, value="5").grid(row=2, column=4)

        # Create radiobuttons for "Line Color:" Black, Red, and Blue
        self.color=StringVar()
        self.color.set("black")
        Radiobutton(self, text="Black", variable=self.color, value="black").grid(row=3, column=2)
        Radiobutton(self, text="Red", variable=self.color, value="red").grid(row=3, column=3)
        Radiobutton(self, text="Blue", variable=self.color, value="blue").grid(row=3, column=4)

        # Create check box button for input numbers
        self.numbers_check = BooleanVar()
        Checkbutton(self, text = "Numbers", variable = self.numbers_check).grid(row=1, column=3, columnspan=2, sticky=E)

        # Insert "roman" pic and make button on it
        self.roman_gif=PhotoImage(file="roman.gif")
        self.button_roman = Button(self, image=self.roman_gif, command=self.letter)
        self.button_roman.grid(row=4, column=2, sticky=W)

        # Inser "random" pic and make button on it
        self.random_gif=PhotoImage(file="random.gif")
        self.button_random = Button(self, image=self.random_gif, command=self.random)
        self.button_random.grid(row=4, column=4, columnspan=2)

        # set X and Y coordinate to start at (20,20)
        self.x, self.y = 20, 20


    def letter(self):
        #entry for putting any numbers into the blank, and mark on the checkbox; it newly save the data into "justin"
        #def letter_value function
            justin = self.number.get()
            if self.numbers_check.get():
                justin = self.letter_value(justin)
                

            for letter in justin:
                width = self.width.get()
                color = self.color.get()
                
                if letter == "M":
                    self.canvas.create_line(self.x, self.y, self.x + 6, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x+14, self.y, self.x + 20, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x+14, self.y+40, self.x + 20, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x + 6, self.y, self.x + 4, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x + 4, self.y, self.x + 4, self.y + 40, width = width, fill = color)
                    self.canvas.create_line(self.x + 16, self.y, self.x + 16, self.y + 40, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y + 40, self.x + 6, self.y + 40, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y, self.x + 6, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x + 6, self.y, self.x + 10, self.y + 20//2, width = width, fill = color)
                    self.canvas.create_line(self.x + 10, self.y + 20//2, self.x + 16, self.y, width = width, fill = color)
                    self.x += 30

                elif letter == "D":
                    self.canvas.create_line(self.x, self.y, self.x, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y, self.x+10, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x+10, self.y, self.x+20, self.y+20//2, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y+40, self.x+10, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x+20, self.y+20//2, self.x+20, self.y+28, width = width, fill = color)
                    self.canvas.create_line(self.x+20, self.y+28, self.x+9, self.y+40, width = width, fill = color)
                    self.x += 30


                elif letter == "C":
                    self.canvas.create_line(self.x+20, self.y, self.x+10, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x+20, self.y+40, self.x+10, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y+10, self.x, self.y+30, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y+10, self.x+11, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y+30, self.x+11, self.y+40, width = width, fill = color)
                    self.x += 30


                elif letter == "L":
                    self.canvas.create_line(self.x, self.y, self.x+10, self.y, width=width, fill=color)
                    self.canvas.create_line(self.x+5, self.y, self.x+5, self.y+40, width=width, fill=color)
                    self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width=width, fill=color)
                    self.x += 30


                elif letter == "X":
                    self.canvas.create_line(self.x, self.y, self.x+20, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x+5, self.y, self.x+15, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x+15, self.y, self.x+5, self.y+40, width = width, fill = color)
                    self.x += 30


                elif letter == "V":        
                    self.canvas.create_line(self.x, self.y, self.x+20, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x+5, self.y, self.x+10, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x+15, self.y, self.x+10, self.y+40, width = width, fill = color)
                    self.x += 30


                    
                elif letter == "I":
                    self.canvas.create_line(self.x, self.y, self.x+20, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x+10, self.y, self.x+10, self.y+40, width = width, fill = color)
                    self.x += 30

                if self.x +30 > 500:
                    self.x = 20
                    self.y +=50


    def random(self):
            justin = self.number.get()
            if self.numbers_check.get():
                justin= self.letter_value(justin)
            
            for letter in justin:
                width = random.choice(["1","2","3","4","5"])
                color = random.choice(["black","red","blue","green"])
                
                if letter == "M":
                    self.canvas.create_line(self.x, self.y, self.x + 6, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x+14, self.y, self.x + 20, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x+14, self.y+40, self.x + 20, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x + 6, self.y, self.x + 4, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x + 4, self.y, self.x + 4, self.y + 40, width = width, fill = color)
                    self.canvas.create_line(self.x + 16, self.y, self.x + 16, self.y + 40, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y + 40, self.x + 6, self.y + 40, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y, self.x + 6, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x + 6, self.y, self.x + 10, self.y + 20//2, width = width, fill = color)
                    self.canvas.create_line(self.x + 10, self.y + 20//2, self.x + 16, self.y, width = width, fill = color)
                    self.x += 30


                elif letter == "D":
                    self.canvas.create_line(self.x, self.y, self.x, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y, self.x+10, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x+10, self.y, self.x+20, self.y+20//2, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y+40, self.x+10, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x+20, self.y+20//2, self.x+20, self.y+28, width = width, fill = color)
                    self.canvas.create_line(self.x+20, self.y+28, self.x+9, self.y+40, width = width, fill = color)
                    self.x += 30


                elif letter == "C":
                    self.canvas.create_line(self.x+20, self.y, self.x+10, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x+20, self.y+40, self.x+10, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y+10, self.x, self.y+30, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y+10, self.x+11, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y+30, self.x+11, self.y+40, width = width, fill = color)
                    self.x += 30


                elif letter == "L":
                    self.canvas.create_line(self.x, self.y, self.x+10, self.y, width=width, fill=color)
                    self.canvas.create_line(self.x+5, self.y, self.x+5, self.y+40, width=width, fill=color)
                    self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width=width, fill=color)
                    self.x += 30


                elif letter == "X":
                    self.canvas.create_line(self.x, self.y, self.x+20, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x+5, self.y, self.x+15, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x+15, self.y, self.x+5, self.y+40, width = width, fill = color)
                    self.x += 30


                elif letter == "V":        
                    self.canvas.create_line(self.x, self.y, self.x+20, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x+5, self.y, self.x+10, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x+15, self.y, self.x+10, self.y+40, width = width, fill = color)
                    self.x += 30


                    
                elif letter == "I":
                    self.canvas.create_line(self.x, self.y, self.x+20, self.y, width = width, fill = color)
                    self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width = width, fill = color)
                    self.canvas.create_line(self.x+10, self.y, self.x+10, self.y+40, width = width, fill = color)
                    self.x += 30

                if self.x +30 > 500:
                    self.x = 20
                    self.y +=50

        

    # if the user selects the number checkbox, they should be able to enter a decimal# & will be conterved to a roman#
    def letter_value(self, justin):
        empty= ""
        
        new_num= int(self.number.get())
        while new_num >=1000:
            empty += "M"
            new_num -= 1000
            
        while new_num >=500:
            empty += "D"
            new_num -= 500

        while new_num >=100:
            empty += "C"
            new_num -= 100
            
        while new_num>=50:
            empty += "L"
            new_num -= 50
            
        while new_num>=10:
            empty += "X"
            new_num -= 10

        while new_num>=5:
            empty += "V"
            new_num -= 5
            
        while new_num>=1:
            empty += "I"
            new_num -= 1

        return empty # allows to save the number into the empty string

# Main
root = Tk()
root.title("Roman Numerals")
root.geometry("900x350")
root.resizable(width = FALSE, height = FALSE)

app=Application(root)
root.mainloop()
