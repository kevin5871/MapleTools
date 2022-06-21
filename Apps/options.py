
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from curses.ascii import isdigit
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter
import sys
import pyglet
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/options")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

pyglet.font.add_file(os.path.join(OUTPUT_PATH, "assets/NEXON Lv2 Gothic.ttf"))

window = Tk()
window.overrideredirect(1)

window.geometry("400x230")
window.configure(bg = "#FFFFFF")

tmpfile = open(OUTPUT_PATH / Path("./assets/variables"), 'r')
tmplist = tmpfile.read().splitlines()
optionvar = list()
for i in range(0,len(tmplist)) :
    if len(tmplist[i]) > 0 :
        if tmplist[i][0] != '#' :
            optionvar.append(tmplist[i])

def savechange() :
    tmpfile = open(OUTPUT_PATH / Path("./assets/variables"), 'w')
    for j in range(0, len(str(charnum.get()))) :
            if isdigit(charnum.get()[j]) != True : 
                charnum.set(0)
                break
    if len(str(charnum.get())) == 9 :
           pass
    else :
        charnum.set(0)

    for j in range(0, len(opacity.get())) :
        if isdigit(str(opacity.get())[j]) != True :
            opacity.set(60)
            break
    if 1 <= int(opacity.get()) and int(opacity.get()) <= 100 :
        pass
    else :
        opacity.set(60)


    tmpfile.write('# Variables File\n# ============================\n# AccountID\n\n%s\n\n# Opacity\n\n%f'%(charnum.get(), (int(opacity.get())/100)))
    tmpfile.close()


canvas = Canvas(window,bg = "#FFFFFF",height = 230,width = 400,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)
canvas.create_rectangle(0.0,0.0,400.0,30.0,fill="#FFA13D",outline="")
canvas.create_text(175.0,35.0,anchor="nw",text="설정",fill="#393939",font=("NEXON Lv2 Gothic", 14 * -1))
canvas.create_text(20.0,2.5,anchor="nw",text="MapleTools",fill="#FFFFFF",font=("NEXON Lv2 Gothic", 18 * -1))
canvas.create_text(20.0,81.0,anchor="nw",text="메이플스토리 유저 번호",fill="#000000",font=("NEXON Lv2 Gothic", 18 * -1))
canvas.create_text(20.0,140.0,anchor="nw",text="투명도 (1~100)",fill="#000000",font=("NEXON Lv2 Gothic", 18 * -1))
#canvas.create_text(180.0,209.0,anchor="nw",text="Ver : 1.0 / Developer : sfcatz",fill="#000000",font=("NEXON Lv2 Gothic", 16 * -1))
canvas.create_text(20.0,100.0,anchor="nw",text="마이메이플>캐릭터정보 더보기>개발자보기(F12)>\n찾기(Ctrl+F) >‘value’ 입력>\n메이플ID 옆 번호 9자리 입력 (<option value=”xxxxxxxxx” ...)",fill="#AAAAAA",font=("NEXON Lv2 Gothic", 9 * -1))

opacity = tkinter.StringVar(value=str(float(optionvar[1])*100))
charnum = tkinter.StringVar(value=optionvar[0])

#charnum.trace("w", savecharnum)
#opacity.trace("w", saveopacity)


entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(305.0,93.0,image=entry_image_1)
entry_1 = Entry(bd=0,bg="#DDDDDD",highlightthickness=0, textvariable=charnum, font=("Nexon Lv2 Gothic", 16 * -1))
entry_1.place(x=225.0,y=78.0,width=160.0,height=28.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(305.0,148.0,image=entry_image_2)
entry_2 = Entry(bd=0,bg="#DDDDDD",highlightthickness=0, textvariable=opacity, font=("Nexon Lv2 Gothic", 16 * -1))
entry_2.place(x=225.0,y=133.0,width=160.0,height=28.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: savechange(), relief="flat")
button_1.place(x=250.0, y=180.0, width=120.0, height=25.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command= lambda : sys.exit(0))
button_3.place(x=345.0, y=2.5, width=50.0, height=25.0)

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
    window.geometry("+%s+%s" % (x , y))

def on_start_hover(event) :
    window.attributes('-alpha', 1.0)

def on_end_hover(event) :
    window.attributes('-alpha', (float(opacity.get()) / 100))


window.resizable(False, False)
window.attributes('-topmost', True)
window.attributes('-alpha', (float(opacity.get()) / 100))
window.bind('<Button-1>', SaveLastClickPos)
window.bind('<B1-Motion>', Dragging)
window.bind('<Enter>', on_start_hover)
window.bind('<Leave>', on_end_hover)
window.mainloop()