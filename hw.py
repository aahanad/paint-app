from tkinter import*
from tkinter import PhotoImage
from PIL import Image,ImageTk
import random 
from tkinter import messagebox  
screen=Tk()
screen.title("halloween")
screen.geometry("468x837")
image=Image.open("halloween2.PNG")
image=ImageTk.PhotoImage(image)
score=0
imageLabel=Label(screen,image=image)
imageLabel.place(relwidth=1,relheight=1)
title=Label(screen,text="Trivia",bg="plum1",fg="SpringGreen2",font=("Brush Script",19))
title.place(x=6,y=100)
bad=["Out of which vegetable were Jack O’ Lanterns originally made? \na) turnips \nb) pumpkins \nc) bell peppers","What was the original purpose of the Halloween costume? \na)to look like an evil spirit \nb) to look cool \nc) to avoid attracting the spirits’ attention","In which country did Halloween originate? \na)Germany \nb)Ireland \nc)England"]
good=["turnips","to avoid attracting the spirits","Ireland"]
number=random.randint(0,2)
def select():
    global number
    text=bad[number]
    word.config(text=text)
def reset():
    global number
    number=random.randint(0,2)
    text=bad[number]
    word.config(text=text)
    guess.delete(0,END)
def check():
    global number
    global score
    user_guess=guess.get()
    if  user_guess==good[number]:
        messagebox.showinfo("you got the correct answer🌸✔")
        score=score+1
        amount.config(text=f"score={score}")
        reset()
    else:
        messagebox.showerror(" wrong😭try again💔")
        reset()
word=Label(screen,text="",fg="green",bg="white",font=("Brush Script",10))
word.place(x=30,y=190)
amount=Label(screen,text=f"score={score}",fg="green",bg="plum1",font=("Brush Script",10))
amount.place(x=300,y=50)
Answer=StringVar()
guess=Entry(screen,font=("Brush Script",14),textvariable=Answer)
guess.place(x=120,y=295)
Check=Button(screen,text="check",fg="red",bg="white",font=("Brush Script",14),width=7,relief=GROOVE,command=check)
Check.place(x=190,y=450)
Reset=Button(screen,text="reset",fg="red",bg="white",font=("Brush Script",14),width=7,relief=GROOVE,command=reset)
Reset.place(x=190,y=500)
select()
screen.mainloop()