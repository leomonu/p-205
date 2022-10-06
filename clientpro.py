
from email.mime import image
from glob import glob
import socket
from tkinter import *
from  threading import Thread
from turtle import title
from PIL import ImageTk, Image
import random
import platform
import tkinter as tk
screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None
numberListByIndex = None
playerName = None
nameEntry = None
nameWindow = None
ticketGrid = None
gameWindow = None
currentNumberList = []

def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())
    
    playerWindow()

def playerWindow():
    global gameWindow
    global canvas2
    global screen_width
    global screen_height
    
    
    gameWindow = Tk()
    gameWindow.title("Tambola Game Screen")
    gameWindow.attributes("-fullscreen",True)

    screen_width=gameWindow.winfo_screenwidth()
    screen_height=gameWindow.winfo_screenheight()

    bg=ImageTk.PhotoImage(file="./assets/1.png")

    canvas2 = Canvas(gameWindow,width=500,height=500)
    canvas2.pack(fill="both",expand=True)
    canvas2.create_image(0,0,image=bg,anchor="nw")
    canvas2.create_text(screen_width/2,screen_height/5,text="Tambola Game",font={"Chalkboard SE",80},fill="Blue")

    gameWindow.resizable(True,True)

    gameWindow.mainloop()

def createTicket():
    global gameWindow
    global ticketGrid

    mianLable = Label(gameWindow,width=65,height=16,relief="ridge",borderwidth=5,bg="white")
    mianLable.place(x=95,y=119)

    xPos=105
    yPos=130

    for row in range(0,3):
        rowList=[]
        for col in range(0,9):
            if (platform.system()=='Darwin'):
                boxButton=Button(gameWindow,font={'Chalkborad SE',18},borderwidth=3,pady=23,padx=22,bg='#fff176',highlightbackground='#fff176',activebackground='#c5e1a5')
                boxButton.place(x=xPos,y=yPos)
            else:
                boxButton = tk.Button(gameWindow,font={'Chalkborad SE',30},width=3,height=2,borderwidth=5,bg="#fff176")
                boxButton.place(x=xPos,y=yPos)
            
            rowList.append(boxButton)
            xPos+=64

        ticketGrid.append(rowList)
        xPos=105
        yPos+=82


def placeNumber():
    global ticketGrid
    global currentNumberList

    for row in range(0,3):
        randomColList = []
        counter = 0

        while counter <=4:
            randomCol=random.randint(0,8)
            if(randomCol not in randomColList):
                randomColList.append(randomCol)
                counter+=1
    
        numberContainer = {
        "0":[1,2,3,4,5,6,7,8,9],
        "1":[10,11,12,13,14,15,16,17,18,19],
        "2":[20,21,22,23,24,25,26,27,28,29],
        "3":[30,31,32,33,34,35,36,37,38,39],
        "4":[40,41,42,43,44,45,46,47,48,49],
        "5":{50,51,52,53,54,55,56,57,58,59},
        "6":[60,61,62,63,64,65,66,67,68,69],
        "7":[70,71,72,73,74,75,76,77,78,79],
        "8":[80,81,82,83,84,85,86,87,88,89],
        }

        counter = 0
        while(counter<len(randomColList)):
            colNum=randomColList[counter]
            numberListByIndex = numberContainer[str(colNum)]
            randomNumber=random.choice(numberListByIndex)

            if(randomNumber not in currentNumberList):
                numberBox=ticketGrid[row][colNum]
                numberBox.configure(text=randomNumber,fg="black")
                currentNumberList.append(randomNumber)

                counter +=1

def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow 
    global canvas1 
    global  screen_height
    global screen_width

    nameWindow = Tk()
    nameWindow.title("Tambola Game")
    nameWindow.attributes("-fullscreen",True)

    screen_width = nameWindow.winfo_screenwidth()
    screen_height=nameWindow.winfo_screenheight()

    bg=ImageTk.PhotoImage(file="./assets/download.jpg")

    canvas1 = Canvas(nameWindow,width=500,height=500)
    canvas1.pack(fill="both",expand=True)
    canvas1.create_image(850,700,image=bg,anchor="nw")
    canvas1.create_text(screen_width/2,screen_height/5,text="ENTER NAME",font={"Chalkboard SE",80},fill="blue")

    nameEntry=Entry(nameWindow,width=25,justify="center",font={"Chalkboard SE",90},bg="white")
    nameEntry.place(x=screen_width/2-100,y=screen_height/3)    

    button= Button(nameWindow,text="save",font={"Chalkboard SE",90},bg="yellow",command=saveName)
    button.place(x=screen_width/2-30,y=screen_height/2)

    nameWindow.resizable(True,True)


    nameWindow.mainloop()

def recivedMsg():
    pass

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 8000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    # Creating First Window
    askPlayerName()




setup()
