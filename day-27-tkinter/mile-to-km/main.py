from tkinter import *


def calculate():
    miles_value = entry_miles.get()
    km_conversion = float(miles_value) * 1.609
    conversion.config(text=f"{km_conversion}")


window = Tk()
window.minsize(width=200, height=200)
window.config(padx=40, pady=40)


#input
entry_miles = Entry(width=10)
entry_miles.focus()
entry_miles.insert(END, "0")
entry_miles.grid(column=1, row=0)


#labels
miles = Label(text="Miles")
miles.grid(column=2, row=0)

equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)

conversion = Label(text="0")
conversion.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)


#button

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()
