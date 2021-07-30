import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkinter import font




# def peopleCounter(text):
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = 'Counter'
        self.geometry("400x250")
        self.count = 0
        self.configure(
            # bg = '#302F2F' # Dark Gray
            bg = 'white'
        )
        self.resizable(False, False)

        ## LABELS
        # Making our font tuples

        self.lbl_Title_font = font.Font(
            family = "Tisa",
            size = 20,
            weight = "bold",
            slant = "italic"
        )
        self.lbl_Counter_font = font.Font(
            family = "Tisa",
            size = 20,
            weight = "bold",
            slant = "italic"
        )

        self.lbl_Title = tk.Label(
            text = 'Pedestrian Counter',
            fg = 'black',
            # bg = '#302F2F',
            bg = 'white',
            master = self,
        )

        self.lbl_Counter = tk.Label(
            fg = 'red',
            bg = 'white',
            text = self.count,
            master = self,

        )
        # using the font tuple here
        self.lbl_Title.configure(font = self.lbl_Title_font) 
        self.lbl_Counter.configure(font = self.lbl_Counter_font)

        self.lbl_Title.place(
            x = 70, 
            y = 40
        )
        self.lbl_Counter.place(
            x = 150,
            y = 120
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()

