import tkinter.
from tkinter import *


class EraseText(tkinter.Frame):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.window.title("Dangerous Writing App")
        self.window.minsize(width=400, height=500)

        self.letters = None
        self.text_label = Text(height=50, width=70)
        self.text_label.pack()
        self.text_label.bind("<Key>", self.handle_wait)

    def handle_wait(self, event):
        if self.letters is not None:
            self.after_cancel(self.letters)

        self.letters = self.after(5000, self.erase_text)

    def erase_text(self):
        self.text_label.delete("1.0", END)


window = Tk()
app = EraseText(window)
app.mainloop()
