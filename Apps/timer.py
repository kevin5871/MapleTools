
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/timer")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("400x230")
window.configure(bg = "#FFFFFF")
window.overrideredirect(1)


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 230,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    400.0,
    30.0,
    fill="#FFA13D",
    outline="")

canvas.create_text(
    175.0,
    35.0,
    anchor="nw",
    text="Timer",
    fill="#393939",
    font=("NEXON Lv2 Gothic", 18 * -1)
)

canvas.create_text(
    20.0,
    2.5,
    anchor="nw",
    text="MapleTools",
    fill="#FFFFFF",
    font=("Nexon Lv2 Gothic", 18 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    70.0,
    122.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#DDDDDD",
    highlightthickness=0
)
entry_1.place(
    x=20.0,
    y=102.0,
    width=100.0,
    height=38.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    200.0,
    123.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#DDDDDD",
    highlightthickness=0
)
entry_2.place(
    x=150.0,
    y=103.0,
    width=100.0,
    height=38.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    330.0,
    123.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#DDDDDD",
    highlightthickness=0
)
entry_3.place(
    x=280.0,
    y=103.0,
    width=100.0,
    height=38.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=45.0,
    y=65.0,
    width=50.0,
    height=25.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=45.0,
    y=154.0,
    width=50.0,
    height=25.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=305.0,
    y=155.0,
    width=50.0,
    height=25.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=175.0,
    y=66.0,
    width=50.0,
    height=25.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=175.0,
    y=155.0,
    width=50.0,
    height=25.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=305.0,
    y=66.0,
    width=50.0,
    height=25.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=162.0,
    y=198.0,
    width=75.0,
    height=20.0
)

canvas.create_text(
    45.0,
    65.0,
    anchor="nw",
    text="UP",
    fill="#000000",
    font=("NEXON Lv2 Gothic", 12 * -1)
)

canvas.create_text(
    45.0,
    154.0,
    anchor="nw",
    text="DOWN",
    fill="#000000",
    font=("NEXON Lv2 Gothic", 12 * -1)
)

canvas.create_text(
    175.0,
    66.0,
    anchor="nw",
    text="UP",
    fill="#000000",
    font=("NEXON Lv2 Gothic", 12 * -1)
)

canvas.create_text(
    175.0,
    155.0,
    anchor="nw",
    text="DOWN",
    fill="#000000",
    font=("NEXON Lv2 Gothic", 12 * -1)
)

canvas.create_text(
    305.0,
    66.0,
    anchor="nw",
    text="UP",
    fill="#000000",
    font=("NEXON Lv2 Gothic", 12 * -1)
)

canvas.create_text(
    305.0,
    155.0,
    anchor="nw",
    text="DOWN",
    fill="#000000",
    font=("NEXON Lv2 Gothic", 12 * -1)
)

canvas.create_text(
    131.0,
    108.0,
    anchor="nw",
    text=":",
    fill="#000000",
    font=("NEXON Lv2 Gothic", 24 * -1)
)

canvas.create_text(
    261.0,
    108.0,
    anchor="nw",
    text=":",
    fill="#000000",
    font=("NEXON Lv2 Gothic", 24 * -1)
)

canvas.create_text(
    162.0,
    198.0,
    anchor="nw",
    text="Start / Stop",
    fill="#000000",
    font=("NEXON Lv2 Gothic", 12 * -1)
)
def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
    window.geometry("+%s+%s" % (x , y))

window.resizable(False, False)
window.attributes('-topmost', True)
window.bind('<Button-1>', SaveLastClickPos)
window.bind('<B1-Motion>', Dragging)
window.mainloop()