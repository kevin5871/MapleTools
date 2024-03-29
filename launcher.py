import subprocess
import tkinter
from tkinter import Canvas, PhotoImage, Button
from pathlib import Path
import sys
import os
from tkinter import messagebox
import csv

#https://www.flaticon.com/free-icon/battle_1732468#
#https://toppng.com/vector-free-download-clock-svg-sand-sand-watch-icon-PNG-free-PNG-Images_163782
#https://www.pngrepo.com/svg/111206/settings
#http://simpleicon.com/power-symbol-2.html

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./Apps/assets/launcher")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

MainColor = None
SubColor = None

tmpfile = open(OUTPUT_PATH / Path("./Apps/assets/variables"), encoding='utf-8')
tmplist = tmpfile.read().splitlines()
optionvar = list()
for i in range(0,len(tmplist)) :
    if len(tmplist[i]) > 0 :
        if tmplist[i][0] != '#' :
            optionvar.append(tmplist[i])
theme = str(optionvar[2])

def OpenData() :
    global Data
    tmpfile = open(OUTPUT_PATH / Path("./Apps/assets/data/theme.csv"), encoding='utf-8')
    DataList = csv.reader(tmpfile, delimiter=",", doublequote=False, lineterminator="\r\n", quotechar="'", skipinitialspace=True)
    Data = list(DataList)
    tmpfile.close()

def SetTheme() :
    global Data, MainColor, SubColor
    for i in range(1, len(Data), 1) :
        if Data[i][0] == theme :
            MainColor = Data[i][1]
            SubColor = Data[i][2]
    if MainColor == None :
        print('Error')

OpenData()
SetTheme()

window = tkinter.Tk()
canvas = Canvas(window, bg='#ffffff', height=400, width=300, bd=0, highlightthickness=0, relief='ridge')
canvas.place(x=0,y=0)
canvas.create_rectangle(0,0,300,400,fill=MainColor,outline="")
canvas.create_text(75, 30, anchor="nw", text="MapleTools", fill="#FFFFFF", font=("NEXON Lv2 Gothic", 30 * -1))
canvas.create_text(110, 65, anchor="nw", text="Ver 1.3 / KMS 1.2.368", fill="#FFFFFF", font=("NEXON Lv2 Gothic", 12 * -1))

window.title('MapleTools')
window.geometry("300x400")

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,command= lambda: subprocess.Popen(['python.exe',os.path.join(OUTPUT_PATH, os.path.join('Apps','levelup.py'))]), relief="flat")
button_1.place(x=15.0, y=100.0, width=130.0, height=130.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_5.png"))
#button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command= lambda: subprocess.Popen(['python.exe',os.path.join(OUTPUT_PATH, os.path.join('Apps','timer.py'))]), relief="flat")
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command= lambda: subprocess.Popen(['python.exe',os.path.join(OUTPUT_PATH, os.path.join('Apps','growportion.py'))]), relief="flat")
button_2.place(x=155.0, y=100.0, width=130.0, height=130.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command= lambda: subprocess.Popen(['python.exe',os.path.join(OUTPUT_PATH, os.path.join('Apps','options.py'))]),relief="flat")
button_3.place(x=15.0, y=240.0, width=130.0, height=130.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, command= lambda:sys.exit(0), relief="flat")
button_4.place(x=155.0, y=240.0, width=130.0, height=130.0)
window.mainloop()