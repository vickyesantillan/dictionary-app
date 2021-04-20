# Practice of tkinter library

from tkinter import *

windows = Tk()


def convert():
    pounds = float(kg_value.get()) * 2.20462
    print('pounds:', pounds)
    pounds1.insert(END, pounds)

    grams = float(kg_value.get()) * 1000
    print('grams: ', grams)
    grams1.insert(END, grams)

    ounces = float(kg_value.get()) * 35.274
    print('ounces:', ounces)
    ounces1.insert(END, ounces)


convert = Button(windows, text="Convert", command=convert)
convert.grid(row=0, column=2)

kg_value = StringVar()
kg = Entry(windows, textvariable=kg_value)
kg.grid(row=0, column=1)

Kg_label = Label(windows, text="Kg")
Kg_label.grid(row=0, column=0)


grams1 = Text(windows, height=1, width=10)
grams1.grid(row=1, column=0)

pounds1 = Text(windows, height=1, width=10)
pounds1.grid(row=1, column=1)

ounces1 = Text(windows, height=1, width=10)
ounces1.grid(row=1, column=2)


windows.mainloop()
