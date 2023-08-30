from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=500, height=300)
#window.configure(background="white")
window.wm_attributes("-transparent", True)
window.config(padx=20,pady=20)
# Label
label = Label(text="I am a label", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)
# change label text
label["text"] = "New Text"
label.config(text="New text")
label.config(pady=50,padx=50)

def button_click():
    input_value = input_field.get()
    label.config(text=input_value)
# Button
button_1 = Button(text="Click me", command=button_click)
button_1.grid(column=1, row=1)

button_2 = Button(text="new button", command=button_click)
button_2.grid(column=2, row=0)

# Entry
input_field = Entry(width=10)
input_field.grid(column=3, row=2)



window.mainloop()