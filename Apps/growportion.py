from ast import Sub
import os
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, messagebox, ttk
import tkinter
import sys
import tempfile
from pyparsing import Char
import requests
import socket
from PIL import Image, ImageTk
from GetCharInfo import GetCharInfo
import regex
import math
import csv
import pyglet

#https://www.inven.co.kr/board/maple/2304/26769

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/growpotion")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

tmpfile = open(OUTPUT_PATH / Path("./assets/variables"), encoding='utf-8')
tmplist = tmpfile.read().splitlines()
optionvar = list()
for i in range(0,len(tmplist)) :
    if len(tmplist[i]) > 0 :
        if tmplist[i][0] != '#' :
            optionvar.append(tmplist[i])
opacity = float(optionvar[1])
theme = str(optionvar[2])
#print(theme.decode())

#print(opacity)
tpfile = tempfile.TemporaryDirectory()
Data = None
Data2 = None

MainColor = None
SubColor = None
pyglet.font.add_file(os.path.join(OUTPUT_PATH, "assets/NEXON Lv2 Gothic.ttf"))

def close() :
    tpfile.cleanup()
    sys.exit(0)

def charset() :
    global useDefChar
    #print(1, useDefChar.get())
    if optionvar[0] != str(0) and socket.gethostbyname(socket.gethostname()) != '127.0.0.1' and useDefChar.get() == True :
        char = GetCharInfo(int(optionvar[0]))
        #print(char)
        #print(char['Exp'])
        a = requests.get(char['AvatarImgURL'])
        if(a.status_code != 200) :
            print(a.status_code)
            messagebox.showerror(title="Network Error", message="인터넷 연결을 확인해주세요. (%d)"%a.status_code)
            return('200','0.0',None)
        #print(a.status_code)
        avatar = open(os.path.join(tempfile.gettempdir(), 'avatar.png'), 'wb')
        avatar.write(a.content)
        avatar.close()
        avatar = Image.open(os.path.join(tempfile.gettempdir(), 'avatar.png'))
        avatar = avatar.resize((80,80))
        avatartk = ImageTk.PhotoImage(avatar)
        e = requests.get("http://wachan.me/exp_api.php?exp1=%s&option=n"%char["Lev"])
        ej = e.json()
        percent = round(int(char['Exp']) / int(ej['result']) * 100, 3)
        #print(percent)
        return (char["Lev"], str(percent), avatartk)
    else :
        if(optionvar[0] == str(0)) :
            messagebox.showerror(title="Setting Error", message="설정에서 대표캐릭터 ID를 확인해주세요")
        elif(socket.gethostbyname(socket.gethostname()) == '127.0.0.1') :
            messagebox.showerror(title="Network Error", message="인터넷 연결을 확인해주세요.")
        elif useDefChar.get() == True :
            messagebox.showerror(title="Error", message="일반 오류.")
        else : 
            pass
        return ('200', '0.0', None)

def calculate(*args) :
    global Data
    if regex.search('[a-zA-Z]', level.get()) :
        level.set(regex.sub('\D', '', level.get()))
    try :
        if int(level.get()) > 299 :
            level.set('200')
    except :
        pass

    if regex.search('[a-zA-Z]', exp.get()) :
            exp.set(regex.sub('[^0-9.]', '', exp.get()))
    try :
        if math.floor(float(exp.get())) >= 10 and len(exp.get()) > 6 :
            exp.set(exp.get()[:6])
        if math.floor(float(exp.get())) < 10 and len(exp.get()) > 5 :
            exp.set(exp.get()[:5])
        if float(exp.get()) > 99.999 :
            exp.set('0.0')
    except :
        pass

    if regex.search('[a-zA-Z]', potion1.get()) :
        potion1.set(regex.sub('\D', '', potion1.get()))
    try :
        if int(potion1.get()) > 50 :
            potion1.set('50')
    except :
        pass

    if regex.search('[a-zA-Z]', potion2.get()) :
        potion1.set(regex.sub('\D', '', potion2.get()))
    try :
        if int(potion2.get()) > 50 :
            potion2.set('50')
    except :
        pass

    if regex.search('[a-zA-Z]', potion3.get()) :
        potion3.set(regex.sub('\D', '', potion3.get()))
    try :
        if int(potion3.get()) > 50 :
            potion3.set('50')
    except :
        pass

    if regex.search('[a-zA-Z]', typhoon.get()) :
        typhoon.set(regex.sub('\D', '', typhoon.get()))
    try :
        if int(typhoon.get()) > 50 :
            typhoon.set('50')
    except :
        pass

    if regex.search('[a-zA-Z]', magnificent.get()) :
        magnificent.set(regex.sub('\D', '', magnificent.get()))
    try :
        if int(magnificent.get()) > 50 :
            magnificent.set('50')
    except :
        pass
    #print(Data)

    try :
        aflevel = int(level.get())
        for i in range(1, len(Data)) :
            if Data[i][0] == level.get() :
                lvlindex = i
        afexp = float(exp.get()) / 100 * int(Data[lvlindex][1]) 

        for i in range(0, int(potion1.get())) :
            if aflevel < 210 :
                aflevel = aflevel + 1
                lvlindex = lvlindex + 1
            else :
                afexp = afexp + int(Data[10][1]) # 210
                if afexp > int(Data[lvlindex][1]) :
                    afexp = afexp - int(Data[lvlindex][1])
                    lvlindex = lvlindex + 1
                    aflevel = aflevel + 1
        
        for i in range(0, int(potion2.get())) :
            if aflevel < 220 :
                aflevel = aflevel + 1
                lvlindex = lvlindex + 1
            else :
                afexp = afexp + int(Data[20][1]) # 220
                if afexp > int(Data[lvlindex][1]) :
                    afexp = afexp - int(Data[lvlindex][1])
                    lvlindex = lvlindex + 1
                    aflevel = aflevel + 1

        for i in range(0, int(potion3.get())) :
            if aflevel < 230 :
                aflevel = aflevel + 1
                lvlindex = lvlindex + 1
            else :
                afexp = afexp + int(Data[30][1]) # 230
                if afexp > int(Data[lvlindex][1]) :
                    afexp = afexp - int(Data[lvlindex][1])
                    lvlindex = lvlindex + 1
                    aflevel = aflevel + 1

        for i in range(0, int(typhoon.get())) :
            if aflevel < 240 :
                aflevel = aflevel + 1
                lvlindex = lvlindex + 1
            else :
                afexp = afexp + int(Data[40][1]) # 240
                if afexp > int(Data[lvlindex][1]) :
                    afexp = afexp - int(Data[lvlindex][1])
                    lvlindex = lvlindex + 1
                    aflevel = aflevel + 1

        for i in range(0, int(magnificent.get())) :
            if aflevel < 250 :
                aflevel = aflevel + 1
                lvlindex = lvlindex + 1
            else :
                afexp = afexp + int(Data[50][1]) # 250
                if afexp > int(Data[lvlindex][1]) :
                    afexp = afexp - int(Data[lvlindex][1])
                    lvlindex = lvlindex + 1
                    aflevel = aflevel + 1
        #print(afexp, aflevel, (afexp / int(Data[lvlindex][1]))*100)
        draw(aflevel, round((afexp / int(Data[lvlindex][1]))*100, 3))
    except :
        #print (-1, -1, -1)
        #print(1)
        draw(-1, -1)

def draw(level, percent) :
    #print(1, level, percent)
    global canvas, ChangeBar, ChangeInfo
    if level != -1 :
        x = round(398 * percent/100)
        canvas.itemconfig(ChangeInfo, text="%s레벨 / %s%%"%(level,percent))
        canvas.coords(ChangeBar, 2,217,x,227)

def pre() :
    global canvas, ChangeBar, ChangeInfo, CharImg, avatartk
    #print(CharImg)
    lvl, exp1, avatartk = charset()
    if avatartk != None :
        CharImg.configure(image=avatartk)
    level.set(lvl)
    exp.set(exp1)
    percent = float(exp.get())
    draw(lvl, percent)

def OpenData() :
    global Data, Data2
    tmpfile = open(OUTPUT_PATH / Path("./assets/data/exp.csv"), encoding='utf-8')
    DataList = csv.reader(tmpfile, delimiter=",", doublequote=False, lineterminator="\r\n", quotechar="'", skipinitialspace=True)
    Data = list(DataList)
    tmpfile.close()

    tmpfile = open(OUTPUT_PATH / Path("./assets/data/theme.csv"), encoding='utf-8')
    DataList = csv.reader(tmpfile, delimiter=",", doublequote=False, lineterminator="\r\n", quotechar="'", skipinitialspace=True)
    Data2 = list(DataList)
    tmpfile.close()

def SetTheme() :
    global Data2, MainColor, SubColor
    for i in range(1, len(Data2), 1) :
        if Data2[i][0] == theme :
            MainColor = Data2[i][1]
            SubColor = Data2[i][2]
    if MainColor == None :
        print('Error')

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

OpenData()
SetTheme()

window = Tk()
window.overrideredirect(1)

window.geometry("400x230")
window.configure(bg = "#FFFFFF")

canvas = Canvas(window,bg = "#FFFFFF",height = 230,width = 400,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)
canvas.create_rectangle(0.0,0.0,400.0,30.0,fill=MainColor,outline="")
canvas.create_rectangle(0.0,30.0,400.0,32.0,fill=SubColor,outline="")
canvas.create_rectangle(0.0,0.0,398.0,228.0,fill='', outline=MainColor, width=3)
canvas.create_text(20.0,2.5,anchor="nw",text="MapleTools",fill="#FFFFFF",font=("NEXON Lv2 Gothic", 18 * -1))
canvas.create_text(175.0, 40.0, anchor="nw", text="익성비", fill="#393939", font=("NEXON Lv2 Gothic", 18 * -1))

button_image_3 = Image.open(relative_to_assets("button_3.png")).convert('RGB')
for i in range(0,button_image_3.size[0]) :
    for j in range(0, button_image_3.size[1]) :
        data = button_image_3.getpixel((i,j))
        if(data == hex_to_rgb('#FFA13D')) :
            button_image_3.putpixel((i,j), hex_to_rgb(MainColor))
buttontk = ImageTk.PhotoImage(image=button_image_3)
button_3 = Button(image=buttontk, borderwidth=0, highlightthickness=0, command= lambda : close())
button_3.place(x=345.0, y=2.5, width=50.0, height=25.0)
useDefChar = tkinter.BooleanVar()
tkinter.Checkbutton(window, variable=useDefChar, text="대표캐릭터 사용", font=("NEXON Lv2 Gothic",16 * -1), command=pre, activebackground="#FFFFFF", background="#FFFFFF").place(x=250, y=100)

# 입력창

level = tkinter.StringVar()
level.trace_add("write", calculate)
canvas.create_text(10, 130, anchor="nw", text="레벨", fill="#000000", font=("NEXON Lv2 Gothic", 16 * -1))
Entry(window, textvariable=level, font=('NEXON Lv2 Gothic', 16*-1), width=10 ).place(x=45,y=130)

exp = tkinter.StringVar()
exp.trace_add("write", calculate)
canvas.create_text(150, 130, anchor="nw", text="경험치(소숫점포함)", fill="#000000", font=("NEXON Lv2 Gothic", 16 * -1))
Entry(window, textvariable=exp, font=('NEXON Lv2 Gothic', 16*-1), width=12 ).place(x=280,y=130)


potion1 = tkinter.StringVar()
potion1.set('0')
potion1.trace_add("write", calculate)
canvas.create_text(5, 160, anchor="nw", text="1비약", fill="#000000", font=("NEXON Lv2 Gothic", 16 * -1))
Entry(window, textvariable=potion1, font=('NEXON Lv2 Gothic', 16*-1), width=3 ).place(x=45,y=160)

potion2 = tkinter.StringVar()
potion2.set('0')
potion2.trace_add("write", calculate)
canvas.create_text(85, 160, anchor="nw", text="2비약", fill="#000000", font=("NEXON Lv2 Gothic", 16 * -1))
Entry(window, textvariable=potion2, font=('NEXON Lv2 Gothic', 16*-1), width=3 ).place(x=125,y=160)

potion3 = tkinter.StringVar()
potion3.set('0')
potion3.trace_add("write", calculate)
canvas.create_text(160, 160, anchor="nw", text="3비약", fill="#000000", font=("NEXON Lv2 Gothic", 16 * -1))
Entry(window, textvariable=potion3, font=('NEXON Lv2 Gothic', 16*-1), width=3 ).place(x=205,y=160)

typhoon = tkinter.StringVar()
typhoon.set('0')
typhoon.trace_add("write", calculate)
canvas.create_text(243, 160, anchor="nw", text="태성비", fill="#000000", font=("NEXON Lv2 Gothic", 16 * -1))
Entry(window, textvariable=typhoon, font=('NEXON Lv2 Gothic', 16*-1), width=3 ).place(x=285,y=160)

magnificent = tkinter.StringVar()
magnificent.set('0')
magnificent.trace_add("write", calculate)
canvas.create_text(323, 160, anchor="nw", text="극성비", fill="#000000", font=("NEXON Lv2 Gothic", 16 * -1))
Entry(window, textvariable=magnificent, font=('NEXON Lv2 Gothic', 16*-1), width=3 ).place(x=365,y=160)
canvas.create_rectangle(0.0, 185.0, 400.0, 186.0, fill="#C4C4C4", outline="")
avatartk = None
ChangeInfo = canvas.create_text(130.0, 190.0, anchor="nw", text="%%s레벨 / %%s%%", fill="#393939", font=("NEXON Lv2 Gothic", 15 * -1))
ChangeBar = canvas.create_rectangle(2,220,2,280, fill=SubColor, outline="")
CharImg = tkinter.Label(window, image=avatartk, background="#FFFFFF")
CharImg.place(x=150, y=40)
#percent = 16.214
pre()

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
    window.attributes('-alpha', opacity)

window.resizable(False, False)
window.attributes('-topmost', True)
window.attributes('-alpha', opacity)
window.bind('<Button-1>', SaveLastClickPos)
window.bind('<B1-Motion>', Dragging)
window.bind('<Enter>', on_start_hover)
window.bind('<Leave>', on_end_hover)
window.mainloop()
