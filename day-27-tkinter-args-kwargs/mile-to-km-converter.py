from tkinter import *
import math


def calculate():
    miles = float(input_mile.get())
    km = math.ceil(miles * 1.60934)
    converted_value_label.config(text=km)


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=150)
window.config(padx=50,pady=50)

input_mile = Entry(width=10)
input_mile.grid(column=3, row=1)
miles_label = Label(text="Miles")
miles_label.grid(column=4, row=1)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=2, row=2)
converted_value_label = Label(text="0")
converted_value_label.grid(column=3,row=2)
km_label = Label(text="Km")
km_label.grid(column=4, row=2)

calculate_button = Button(text="Calculate",command=calculate)
calculate_button.grid(column=3, row=3)

window.mainloop()