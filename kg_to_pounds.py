# Practice of tkinter library


from tkinter import *

# Create a Tinker windows

windows = Tk()

# Convert Function


def convert():

    pounds1.delete("1.0", END)  # Deleting the old value
    pounds = round(float(kg_value.get()) * 2.20462, 2)
    pounds1.insert(END, pounds)

    grams1.delete("1.0", END)  # Deleting the old value
    grams = round(float(kg_value.get()) * 1000, 2)
    grams1.insert(END, grams)

    ounces1.delete("1.0", END)  # Deleting the old value
    ounces = round(float(kg_value.get()) * 35.274, 2)
    ounces1.insert(END, ounces)

# Convert botton


convert = Button(windows, text="Convert", command=convert)
convert.grid(row=0, column=2)

# Kg entry value
kg_value = StringVar()
kg = Entry(windows, textvariable=kg_value)
kg.grid(row=0, column=1)

# Kg label
Kg_label = Label(windows, text="Kg➡")
Kg_label.grid(row=0, column=0)

# grams label
grams_label = Label(windows, text="Grams")
grams_label.grid(row=1, column=0)

# pounds label
pounds_label = Label(windows, text="Pounds")
pounds_label.grid(row=1, column=1)

# ounces label
ounces_label = Label(windows, text="Ounces")
ounces_label.grid(row=1, column=2)


# Converts results

grams1 = Text(windows, height=1, width=20)
grams1.grid(row=2, column=0)

pounds1 = Text(windows, height=1, width=20)
pounds1.grid(row=2, column=1)

ounces1 = Text(windows, height=1, width=20)
ounces1.grid(row=2, column=2)


windows.mainloop()
