from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox as mb
from BOT import boardevaluation,decision,decision1
import time,pygame

#==================DECLARED GLOBAL VARIABLES=============================
c=True
count=30
timer=30
bot=True
bot1=True
resume=False
audio=1
sound=1
player1="Player_1"
player2="Bot_69"
m=20
v=70
colseq=0

def quit():
    sound2.play(0)
    if mb.askyesno("TIC-TAC-TOE","Confirm if you want to quit") >0 :
        wn.destroy()
        sound1.stop()
        return
    
def startgame():
    global c,count,resume,timer
    b1["text"],b1["image"]="",img8
    b2["text"],b2["image"]="",img8
    b3["text"],b3["image"]="",img8
    b4["text"],b4["image"]="",img8
    b5["text"],b5["image"]="",img8
    b6["text"],b6["image"]="",img8
    b7["text"],b7["image"]="",img8
    b8["text"],b8["image"]="",img8
    b9["text"],b9["image"]="",img8
    c=True
    count=timer
    resume=True
    update_clock()
    switch(game)

def update_clock():
    global count,resume,player1,player2
    if count==0:
        if 8 not in convert():
            msg.set("MATCH TIE!")
        elif c:
            msg.set(player2+"  WON!")
        else:
            msg.set(player1+"  WON!")
        label["text"]="Time left : 0"
        switch(restart)
        return
    if count==-1:
        startgame()
        return
    if count==-2:
        switch(startpage)
        return
    if resume:
        count-=1
    setvar.set("Time left : "+str(count))
    wn.after(1000, update_clock)
    
wn=Tk()
wn.geometry("800x600")
wn.title("TIC-TAC-TOE")
wn.iconbitmap("icon.ico")
wn.resizable(width=False,height=False)
select=Frame(wn)
startpage=Frame(wn)
game=Frame(wn)
restart=Frame(wn)
option=Frame(wn)
gamemenu=Frame(wn)
about=Frame(wn)
pygame.mixer.init()
colour=["green","salmon","pink","goldenrod","cyan"]
colour1=["green2","red","deep pink","yellow","blue2"]

def switch(fr):
    sound2.play(0)
    fr.tkraise()
    
for frame in (startpage,select,game,restart,gamemenu,option,about):
    frame.grid(row = 0, column = 0)

sound1=pygame.mixer.Sound("music/s1.wav")
sound1.set_volume(0.7)
sound2=pygame.mixer.Sound("music/s2.wav")
sound2.set_volume(0.7)
sound3=pygame.mixer.Sound("music/s3.wav")
sound3.set_volume(0.7)
sound4=pygame.mixer.Sound("music/s4.wav")
sound4.set_volume(0.7)
sound5=pygame.mixer.Sound("music/s5.wav")
sound5.set_volume(0.7)
sound1.play(-1)

background_image = ImageTk.PhotoImage(Image.open("background.png"))
img1=ImageTk.PhotoImage(Image.open("ico/img1.png"))
img2=ImageTk.PhotoImage(Image.open("ico/img2.png"))
img3=ImageTk.PhotoImage(Image.open("ico/img3.png"))
img4=ImageTk.PhotoImage(Image.open("ico/img4.jpg"))
img5=ImageTk.PhotoImage(Image.open("ico/back.jpg"))
img6=ImageTk.PhotoImage(Image.open("ico/menu.jpg"))
img7=ImageTk.PhotoImage(Image.open("ico/x.jpg"))
img8=ImageTk.PhotoImage(Image.open("ico/none.png"))
img9=ImageTk.PhotoImage(Image.open("ico/o.jpg"))
img10=ImageTk.PhotoImage(Image.open("ico/player1.jpg"))
img11=ImageTk.PhotoImage(Image.open("ico/player2.jpg"))
img12=ImageTk.PhotoImage(Image.open("ico/vs.jpg"))
img13=ImageTk.PhotoImage(Image.open("ico/img5.png"))


#=================================STARTPAGE=====================================================
dim=(2,25)
f=15
p1id=StringVar()
p1id.set(player1)
background1 = Label(startpage,image=background_image)
background1.pack()
lb1=Label(startpage,image=img13).place(x=180,y=10)

def stopm():
    global audio
    audio=1-audio
    sound2.play(0)
    if audio:
        bt1["image"]=img2
        sound1.set_volume(m/100)
    else:
        bt1["image"]=img1
        sound1.set_volume(0)
        
bt1=Button(startpage,image=img2,command=stopm)
bt1.place(x=5,y=10)

def stopv():
    global sound,v
    sound=1-sound
    sound2.play(0)
    if sound:
        bt2["image"]=img4
        sound2.set_volume(v/100)
        sound3.set_volume(v/100)
        sound4.set_volume(v/100)
        sound5.set_volume(v/100)
    else:
        bt2["image"]=img3
        sound2.set_volume(0)
        sound3.set_volume(0)
        sound4.set_volume(0)
        sound5.set_volume(0)
        
bt2=Button(startpage,image=img4,command=stopv)
bt2.place(x=80,y=10)
bt3=Button(startpage,text="PLAY",bg=colour[colseq],font=("arial",f,"bold"),height=dim[0],width=dim[1],command=lambda: switch(select))

def onB1(event):
    sound3.play(0)
    bt3["bg"]=colour1[colseq]

def offB1(event):
    bt3["bg"]=colour[colseq]
    
bt3.bind('<Enter>',onB1)
bt3.bind('<Leave>',offB1)
bt3.place(x=270,y=200)
bt4=Button(startpage,text="OPTION",bg=colour[colseq],font=("arial",f,"bold"),height=dim[0],width=dim[1],command=lambda: switch(option))

def onB2(event):
    sound3.play(0)
    bt4["bg"]=colour1[colseq]

def offB2(event):
    bt4["bg"]=colour[colseq]
    
bt4.bind('<Enter>',onB2)
bt4.bind('<Leave>',offB2)
bt4.place(x=270,y=300)
bt5=Button(startpage,text="ABOUT",bg=colour[colseq],font=("arial",f,"bold"),height=dim[0],width=dim[1],command=lambda: switch(about))

def onB3(event):
    sound3.play(0)
    bt5["bg"]=colour1[colseq]

def offB3(event):
    bt5["bg"]=colour[colseq]

bt5.bind('<Enter>',onB3)
bt5.bind('<Leave>',offB3)
bt5.place(x=270,y=400)
bt6=Button(startpage,text="QUIT",bg=colour[colseq],font=("arial",f,"bold"),height=dim[0],width=dim[1],command=quit)

def onB4(event):
    sound3.play(0)
    bt6["bg"]=colour1[colseq]

def offB4(event):
    bt6["bg"]=colour[colseq]

bt6.bind('<Enter>',onB4)
bt6.bind('<Leave>',offB4)
bt6.place(x=270,y=500)
Label(startpage,image=img10).place(x=700,y=80)
Label(startpage,textvar=p1id,fg="blue",bg="pink",font=("arial",12,"bold")).place(x=700,y=150)


#=================================SELECT MODE=====================================================
background2 = Label(select,image=background_image)
background2.pack()
btn3=Button(select,image=img5,border=0,command=lambda: switch(startpage)).place(x=5,y=10)
Label(select,text="Choose The Game Mode",bg="grey",relief="solid",fg="white",font=("arial",15,"bold"),height=2,width=40).place(x=185,y=40)

def checkmode():
    global bot,player2
    bot=False
    player2=(name1.get() if name1.get().strip()!="" else "Player_2")
    p2id.set(player2)
    startgame()
    
btn1=Button(select,text='Vs players',font=("arial",15,"bold"),bg=colour[colseq],height=2,width=20,command=checkmode)

def onB21(event):
    sound3.play(0)
    btn1["bg"]=colour1[colseq]

def offB21(event):
    btn1["bg"]=colour[colseq]

btn1.bind('<Enter>',onB21)
btn1.bind('<Leave>',offB21)
btn1.place(x=285,y=200)

def checkmode1():
    global bot,bot1,player2
    bot=True
    if bot1:
        player2="Bot_32"
    else:
        player2="Bot_69"
    p2id.set(player2)
    startgame()

btn2=Button(select,text='Vs computer',font=("arial",15,"bold"),bg=colour[colseq],height=2,width=20,command=checkmode1)

def onB22(event):
    sound3.play(0)
    btn2["bg"]=colour1[colseq]

def offB22(event):
    btn2["bg"]=colour[colseq]

btn2.bind('<Enter>',onB22)
btn2.bind('<Leave>',offB22)
btn2.place(x=285,y=350)



#=================================GAME=====================================================
background3 = Label(game,image=background_image)
background3.pack()
dim=(5,12)
setvar=StringVar()
p2id=StringVar()
p2id.set(player2)
Label(game,image=img10).place(x=10,y=70)
Label(game,textvar=p1id,fg="blue",bg="pink",font=("arial",12,"bold")).place(x=10,y=150)
Label(game,image=img11).place(x=700,y=70)
Label(game,textvar=p2id,fg="blue",bg="pink",font=("arial",12,"bold")).place(x=700,y=150)
Label(game,image=img12).place(x=340,y=80)
label=Label(game,textvar=setvar, font=('Helvetica', 15), fg='blue')

def save():
    global resume
    resume=False
    switch(gamemenu)
    
Button(game,image=img6,border=0,command=save).place(x=5,y=10)

def click(btn):
    global c,count,timer
    count=timer
    
    if btn["text"]=="" and c==True:
        btn["image"]=img9
        btn["text"]="O"
        c=False
    elif btn["text"]=="" and c==False:
        btn["image"]=img7
        btn["text"]="X"
        c=True
        
    if checkwinner():
        return
    
    if c==False and bot:
         AImove()
        
    checkwinner()
    
def checkwinner():
    global count
    if boardevaluation(convert(),1) or boardevaluation(convert(),0) or (8 not in convert()):
        count=0
        sound1.stop()
        if p1id.get() in msg.get():
             sound4.play(0)
        else:
             sound5.play(0)
        sound1.play(-1)
        return True
        
def convert():
    l=[8 for i in range(9)]
    l[0]=1 if b1["text"]=="X" else (0 if b1["text"]=="O" else 8)
    l[1]=1 if b2["text"]=="X" else (0 if b2["text"]=="O" else 8)
    l[2]=1 if b3["text"]=="X" else (0 if b3["text"]=="O" else 8)
    l[3]=1 if b4["text"]=="X" else (0 if b4["text"]=="O" else 8)
    l[4]=1 if b5["text"]=="X" else (0 if b5["text"]=="O" else 8)
    l[5]=1 if b6["text"]=="X" else (0 if b6["text"]=="O" else 8)
    l[6]=1 if b7["text"]=="X" else (0 if b7["text"]=="O" else 8)
    l[7]=1 if b8["text"]=="X" else (0 if b8["text"]=="O" else 8)
    l[8]=1 if b9["text"]=="X" else (0 if b9["text"]=="O" else 8)
    return l

def AImove():
    global c
    if bot1==True:
        dec=decision1(convert())
    else:
        dec=decision(convert())
    if dec==1:
        b1["text"],b1["image"]="X",img7
    if dec==2:
        b2["text"],b2["image"]="X",img7
    if dec==3:
        b3["text"],b3["image"]="X",img7
    if dec==4:
        b4["text"],b4["image"]="X",img7
    if dec==5:
        b5["text"],b5["image"]="X",img7
    if dec==6:
        b6["text"],b6["image"]="X",img7
    if dec==7:
        b7["text"],b7["image"]="X",img7
    if dec==8:
        b8["text"],b8["image"]="X",img7
    if dec==9:
        b9["text"],b9["image"]="X",img7
    c=True
    
b1=Button(game,image=img8,border=0,command=lambda: click(b1))
b2=Button(game,image=img8,border=0,command=lambda: click(b2))
b3=Button(game,image=img8,border=0,command=lambda: click(b3))
b4=Button(game,image=img8,border=0,command=lambda: click(b4))
b5=Button(game,image=img8,border=0,command=lambda: click(b5))
b6=Button(game,image=img8,border=0,command=lambda: click(b6))
b7=Button(game,image=img8,border=0,command=lambda: click(b7))
b8=Button(game,image=img8,border=0,command=lambda: click(b8))
b9=Button(game,image=img8,border=0,command=lambda: click(b9))
b1.place(x=230,y=220)
b2.place(x=340,y=220)
b3.place(x=460,y=220)
b4.place(x=230,y=330)
b5.place(x=340,y=330)
b6.place(x=460,y=330)
b7.place(x=230,y=440)
b8.place(x=340,y=440)
b9.place(x=460,y=440)
label.place(x=670,y=5)



#=================================GAME OVER=====================================================
background4 = Label(restart,image=background_image)
background4.pack()
msg=StringVar()
rlb=Label(restart,textvar=msg,bg="orange",relief="solid",fg="blue",height=3,width=40,font=("arial",14,"bold")).place(x=160,y=40)
btu1=Button(restart,text="RESTART",bg=colour[colseq],font=("arial",15,"bold"),height=2,width=25,command=startgame)

def onB41(event):
    sound3.play(0)
    btu1["bg"]=colour1[colseq]

def offB41(event):
    btu1["bg"]=colour[colseq]

btu1.bind('<Enter>',onB41)
btu1.bind('<Leave>',offB41)
btu1.place(x=270,y=200)
btu2=Button(restart,text="MAIN MENU",bg=colour[colseq],font=("arial",15,"bold"),height=2,width=25,command=lambda: switch(startpage))

def onB42(event):
    sound3.play(0)
    btu2["bg"]=colour1[colseq]

def offB42(event):
    btu2["bg"]=colour[colseq]
    
btu2.bind('<Enter>',onB42)
btu2.bind('<Leave>',offB42)
btu2.place(x=270,y=300)
btu3=Button(restart,text="QUIT",bg=colour[colseq],font=("arial",15,"bold"),height=2,width=25,command=quit)

def onB43(event):
    sound3.play(0)
    btu3["bg"]=colour1[colseq]

def offB43(event):
    btu3["bg"]=colour[colseq]
    
btu3.bind('<Enter>',onB43)
btu3.bind('<Leave>',offB43)
btu3.place(x=270,y=400)



#=================================GAME MENU=====================================================
background5 = Label(gamemenu,image=background_image)
background5.pack()
Label(gamemenu,text="PAUSED",bg="orange",relief="solid",fg="white",font=("arial",15,"bold"),height=2,width=40).place(x=185,y=40)

def res():
    global resume
    resume=True
    switch(game)
    
rbt1=Button(gamemenu,text="RESUME",bg=colour[colseq],font=("arial",f,"bold"),height=2,width=25,command=res)

def onB31(event):
    sound3.play(0)
    rbt1["bg"]=colour1[colseq]

def offB31(event):
    rbt1["bg"]=colour[colseq]
    
rbt1.bind('<Enter>',onB31)
rbt1.bind('<Leave>',offB31)
rbt1.place(x=270,y=200)

def stopclock():
    global count
    count=-1
    
rbt2=Button(gamemenu,text="RESTART",bg=colour[colseq],font=("arial",f,"bold"),height=2,width=25,command=stopclock)

def onB32(event):
    sound3.play(0)
    rbt2["bg"]=colour1[colseq]

def offB32(event):
    rbt2["bg"]=colour[colseq]

rbt2.bind('<Enter>',onB32)
rbt2.bind('<Leave>',offB32)
rbt2.place(x=270,y=300)

def stopclock1():
    global count
    count=-2
    
rbt3=Button(gamemenu,text="MAIN MENU",bg=colour[colseq],font=("arial",f,"bold"),height=2,width=25,command=stopclock1)

def onB33(event):
    sound3.play(0)
    rbt3["bg"]=colour1[colseq]

def offB33(event):
    rbt3["bg"]=colour[colseq]
    
rbt3.bind('<Enter>',onB33)
rbt3.bind('<Leave>',offB33)
rbt3.place(x=270,y=400)
rbt4=Button(gamemenu,text="QUIT",bg=colour[colseq],font=("arial",f,"bold"),height=2,width=25,command=quit)

def onB34(event):
    sound3.play(0)
    rbt4["bg"]=colour1[colseq]

def offB34(event):
    rbt4["bg"]=colour[colseq]
    
rbt4.bind('<Enter>',onB34)
rbt4.bind('<Leave>',offB34)
rbt4.place(x=270,y=500)



#=================================OPTIONS=====================================================
background6 = Label(option,image=background_image)
background6.pack()
Label(option,text="OPTIONS",bg="orange",relief="solid",fg="blue",height=3,width=40,font=("arial",14,"bold")).place(x=160,y=10)
Label(option,text="Music  : ",font=("arial",16,"bold")).place(x=80,y=150)
music=IntVar()
music.set(70)
Scale(option, from_=0, to=100, orient=HORIZONTAL,width=5,variable=music).place(relx=0.23,rely=0.23,relwidth=0.4)
Label(option,text="Volume : ",font=("arial",16,"bold")).place(x=80,y=250)
volume=IntVar()
volume.set(70)
Scale(option, from_=0, to=100, orient=HORIZONTAL,width=5,variable=volume).place(relx=0.23,rely=0.38,relwidth=0.4)
Label(option,text="Player1 : ",font=("arial",16,"bold")).place(x=80,y=350)
name=StringVar()
name.set("Player_1")
Entry(option,width=17,font=("arial",16,"bold"),textvar=name).place(x=193,y=350)
Label(option,text="Player2 : ",font=("arial",16,"bold")).place(x=433,y=350)
name1=StringVar()
name1.set("Player_2")
Entry(option,width=17,font=("arial",16,"bold"),textvar=name1).place(x=563,y=350)
Label(option,text="Timer  : ",font=("arial",16,"bold")).place(x=80,y=450)
clock=IntVar()
clock.set(30)
Scale(option, from_=1, to=60, orient=HORIZONTAL,width=5,variable=clock).place(relx=0.23,rely=0.68,relwidth=0.4)
Label(option,text="Colour : ",font=("arial",14,"bold")).place(x=620,y=150)
Label(option,text="Level : ",font=("arial",15,"bold")).place(x=620,y=250)
op=StringVar()
level=["EASY","HARD"]
op.set(level[0])
opt=OptionMenu(option, op, *level)
opt.config(width=5,height=1)
opt.place(x=700,y=250)

def swapcolor():
    global colseq
    if colseq==len(colour)-1:
        colseq=0
    else:
        colseq+=1
    col["bg"]=colour[colseq]
    sv["bg"]=colour[colseq]
    bt3["bg"]=colour[colseq]
    bt4["bg"]=colour[colseq]
    bt5["bg"]=colour[colseq]
    bt6["bg"]=colour[colseq]
    btu1["bg"]=colour[colseq]
    btu2["bg"]=colour[colseq]
    btu3["bg"]=colour[colseq]
    btn1["bg"]=colour[colseq]
    btn2["bg"]=colour[colseq]
    rbt1["bg"]=colour[colseq]
    rbt2["bg"]=colour[colseq]
    rbt3["bg"]=colour[colseq]
    rbt4["bg"]=colour[colseq]

col=Button(option,bg=colour[colseq],height=1,width=3,command=swapcolor)
col.place(x=720,y=151)

def setting():
    global m,v,timer,player1,bot1
    sound2.play(0)
    m=music.get()
    v=volume.get()
    timer=clock.get()
    bt1["image"]=img2
    bt2["image"]=img4
    if op.get()==level[0]:
        bot1=True
    else:
        bot1=False
    if name.get().strip()!="Player_1":
        player1=name.get()
        if len(name.get())>10:
            player1=name.get()[:10]
        p1id.set(player1)
    sound1.set_volume(m/100)
    sound2.set_volume(v/100)
    sound3.set_volume(v/100)
    mb.showinfo("Sttings","Settings Applied Successfully!")
    
sv=Button(option,text="Save",bg=colour[colseq],font=("arial",10,"bold"),height=2,width=15,command=setting)
sv.place(x=650,y=500)
Button(option,image=img5,border=0,command=lambda: switch(startpage)).place(x=5,y=5)



#=================================ABOUT=====================================================
background6 = Label(about,image=background_image)
background6.pack()
Label(about,text="ABOUT",bg="orange",relief="solid",fg="blue",height=3,width=40,font=("arial",14,"bold")).place(x=160,y=10)
Label(about,text="TIC-TAC-TOE",bg="gold",relief="solid",fg="deep pink",width=20,font=("arial",15,"bold")).place(x=270,y=130)
Button(about,image=img5,border=0,command=lambda: switch(startpage)).place(x=5,y=5)
info=Text(about,font=("arial",10,"bold"),fg="turquoise1",bg="green4",height=25,width=100)
file=open('info.txt')
info.insert(1.0, file.read())
info["state"]=DISABLED
info.place(x=50,y=180)

startpage.tkraise()

wn.mainloop()