# Practice of tkinter library


from tkinter import *

windows = Tk()

# Convert Function


def convert():
    pounds1.delete("1.0", END)  # Deleting the old value
    pounds = float(kg_value.get()) * 2.20462
    pounds1.insert(END, pounds)

    grams1.delete("1.0", END)  # Deleting the old value
    grams = float(kg_value.get()) * 1000
    grams1.insert(END, grams)

    ounces1.delete("1.0", END)  # Deleting the old value
    ounces = float(kg_value.get()) * 35.274
    ounces1.insert(END, ounces)

# Convert botton


convert = Button(windows, text="Convert", command=convert)
convert.grid(row=0, column=2)

# Kg entry value
kg_value = StringVar()
kg = Entry(windows, textvariable=kg_value)
kg.grid(row=0, column=1)

# Kg label
Kg_label = Label(windows, text="Kg")
Kg_label.grid(row=0, column=0)

# Converts results

grams1 = Text(windows, height=1, width=20)
grams1.grid(row=1, column=0)

pounds1 = Text(windows, height=1, width=20)
pounds1.grid(row=1, column=1)

ounces1 = Text(windows, height=1, width=20)
ounces1.grid(row=1, column=2)


windows.mainloop()
