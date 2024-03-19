from tkinter import *

def button_click():
    print("I got clicked")
    new_text = inputField.get()
    my_label.config(text = new_text)

window = Tk()
window.title("My first GUI Program")
window.minsize(width = 500, height = 500)
window.config(padx = 20,pady = 20)

#Components
#Label
my_label = Label(text = "I am a Label", font = ("Arial",20))
# my_label["text"] = "New text"
my_label.config(text = "New text")
my_label.grid(column = 0, row = 0)

#Button
button = Button(text = "Click Me", command = button_click)
button.grid(column = 1,row = 1)

button_2 = Button(text = "Click me_2",command = button_click)
button_2.grid(column = 2,row = 0)

#Entry
inputField = Entry(width = 10)
print(inputField.get())
inputField.grid(column = 3, row = 2)







window.mainloop()
