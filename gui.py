import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkinter import font
import hog
import people

def select_file(event):
    path = fd.askopenfilename()
    hog.pedestrian_detection_video(path)
    #restart()

global window
window = tk.Tk()
window.title = 'Open File'
window.geometry("800x400")
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
btn_select_image_font = font.Font(
    family = "Tisa",
    size = 15,
    weight = "bold"
)

lbl_Title = tk.Label(
    text = 'Pedestrian Detector',
    fg = 'black',
    # bg = '#302F2F',
    bg = 'white',
    master = window,
)
lbl_Title.configure(font = lbl_Title_font) # using the font tuple here



# Image using Pillow (PIL)

#image - 1
load1 = Image.open("stick.jpg")
load1 = load1.resize((150, 150), Image.ANTIALIAS)
load1 = ImageTk.PhotoImage(load1)

lbl_image1_py = tk.Label(
    image = load1,
    bg = '#302F2F',
    bd = 0
)

#image -2
load2 = Image.open("stick.jpg")
load2 = load2.transpose(Image.FLIP_LEFT_RIGHT)
load2 = load2.resize((150, 150), Image.ANTIALIAS)
load2 = ImageTk.PhotoImage(load2)

lbl_image2_py = tk.Label(
    image = load2,
    bg = '#302F2F',
    bd = 0
)
## Button
btn_select_image = tk.Button(
    
    text = 'Select Media',
    bd = 4,
    bg = '#302F2F',
    fg = 'white',
    #command = fd.askopenfilename()
    highlightcolor = 'black'

)
btn_select_image.bind("<Button-1>",select_file)
btn_select_image.configure(font = btn_select_image_font)



#placing inside window here onwards

lbl_Title.place(
    x = 240, 
    y = 40
)
lbl_image1_py.place(
    x = 0,
    y = 20

)
lbl_image2_py.place(

    x = 650,
    y = 20
)
btn_select_image.place(
    y = 250,
    x = 295
)

window.mainloop()