from tkinter import *
print("Write settings:")
buttontext = input("text for button: ")
titletext = input("text for title: ")

#


window = Tk()
wbutton = Button(window, text = "buttontext")
wbutton.grid(column = 1, row = 0)
window.title("titletext")
window.geometry('int(input("X:")) x int(input("Y:"))')
tag = Label(window, text = "tagtext", font = ("Arial Bold",50))
tag.grid(column = 1, row = 0)
window.mainloop()