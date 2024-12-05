import random

from tkinter import *

window = Tk()

window.geometry("1920x1080")
window.title("Goopys Dice")

def myclick():
    MyLabel = Label(window, text=random.randint(1, 20))
    MyLabel.pack()


label = Label(window, text="welcome to Goopy_GT's dice!", font=("Arial", 20))
button = Button(window, text="roll", font="Arial", command=myclick)

label.pack()
button.pack(pady= 100)



window.mainloop()
