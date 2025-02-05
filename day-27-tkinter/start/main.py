from tkinter import *

window = Tk()

window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    new_label = new_input.get()
    label.config(text=f"{new_label}")


#Label
label = Label(text="This is a Label", font=("Arial", 24, "bold"))
label["text"] = "New Label"
label.grid(column=0, row=0)

#Button
button = Button(text="Click Me")
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry

new_input = Entry(width=10)
new_input.get()
new_input.grid(column=3, row=2)


window.mainloop()