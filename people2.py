import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkinter import font
import time
import hog2
# def counter():

window = tk.Tk()
window.title = 'Counter'
window.geometry("400x250")
# count = 0
window.configure(
    # bg = '#302F2F' # Dark Gray
    bg = 'white'
)
window.resizable(False, False)

## LABELS
# Making our font tuples

lbl_Title_font = font.Font(
    family = "Tisa",
    size = 20,
    weight = "bold",
    slant = "italic"
)
lbl_Counter_font = font.Font(
    family = "Tisa",
    size = 20,
    weight = "bold",
    slant = "italic"
)

lbl_Title = tk.Label(
    text = 'Pedestrian Counter',
    fg = 'black',
    # bg = '#302F2F',
    bg = 'white',
    master = window
)

lbl_Counter = tk.Label(
    fg = 'red',
    bg = 'white',
    text = hog2.,
    master = window,

)
# using the font tuple here
lbl_Title.configure(font = lbl_Title_font) 
lbl_Counter.configure(font = lbl_Counter_font)

lbl_Title.place(
    x = 70, 
    y = 40
)
lbl_Counter.place(
    x = 150,
    y = 120
)
window.mainloop()
# time.sleep(2)
# window.destroy()