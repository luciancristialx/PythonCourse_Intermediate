from tkinter import *

def button_click():
    miles = float(entry_mi.get())
    km = round(miles * 1.609)
    lbl_convert_value.config(text = f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 40, height = 40)
window.config(padx = 30,pady = 30)

lbl_equal = Label()
lbl_equal.config(text = "is equal to",padx=7,pady = 5)
lbl_equal.grid(column = 0,row = 1)

entry_mi = Entry(width = 10)
entry_mi.grid(column = 1,row = 0)
entry_mi.focus()

lbl_mi = Label()
lbl_mi.config(text = "Miles",padx=5)
lbl_mi.grid(column = 2, row = 0)

lbl_convert_value = Label()
lbl_convert_value.config(text = "0")
lbl_convert_value.grid(column = 1, row = 1)

lbl_mi = Label()
lbl_mi.config(text = "Km",padx=10)
lbl_mi.grid(column = 2, row = 1)

btn_calc = Button(text = "Calculate",command = button_click)
btn_calc.grid(column = 1,row = 2)



window.mainloop()