import tkinter as tk
import tkinter.ttk as Ttk

# credits: Stackoverflow answer from 'Henry Yik'
# https://stackoverflow.com/questions/56494188/create-a-simple-function-for-combobox-dialog-in-tkinter
class SimpleChoiceBox:
    def __init__(self, title, text, choices):
        self.t = tk.Toplevel()
        self.t.title(title if title else "")
        self.selection = None
        tk.Label(self.t, text=text if text else "").grid(row=0, column=0)
        self.c = Ttk.Combobox(
            self.t, value=choices if choices else [], state="readonly"
        )
        self.c.grid(row=0, column=1)
        self.c.bind("<<ComboboxSelected>>", self.combobox_select)

    def combobox_select(self, event):
        self.selection = self.c.get()
        self.t.destroy()


def c_funcbutton():
    global res
    res = SimpleChoiceBox(
        "Ask", "What is your favourite fruit?", ["Apple", "Orange", "Watermelon"]
    )
