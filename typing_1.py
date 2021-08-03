from tkinter import *
screen = Tk()
import random
from tkinter import messagebox
  

#############################################################  =>  defining the screen to show

screen.title("Typing Speed")
screen.geometry("800x600+400+100")
screen.configure(bg="powder blue")
screen.iconbitmap("Typing_Checker/type.ico")
screen.minsize(800,600)
screen.maxsize(800,600)


#############################################################  =>  Putting words to show 

words = ['Mango','Apple','Graphs','Banana','Chiku','gun','Fire','Police','Good','Bad','God','Great','Lokmanya','Tilak','College','School','Ground','Laptop','Mouse','Keyboard','Table','Chair','Bed','Mirror','Body','Nose','Hand','Leg','Hand','Mouth','House','Room','Window','Tower','Fan','Air','Python','Java','C','HTML','CSS','Reactjs','MongoDB','Mongoose','Nodejs','Expressjs','Firebase','Strip','MaterialIcon','eTC']


#############################################################  =>  slider function

def labelslider():
    global count,wordslider
    text = 'welcome to typing speed tester ..'
    if(count >= len(text)):
        count = 0
        wordslider = ''
    wordslider += text[count]
    count += 1
    topfontlabel.configure(text=wordslider)
    topfontlabel.after(100,labelslider)


#############################################################  =>  word match function

def matchword(event):
    global score,missed
    if(timeleft == 60):
        time()
    hintlabel.configure(text='')
    if Input.get() == midelfontlabel['text']:
        score+=1
        print("matched",score)
        scorenumberlabel.configure(text=score)
    else:
        missed+=1
        print("not matched",missed)
    random.shuffle(words)
    midelfontlabel.configure(text=words[0])
    Input.delete(0,END)

#############################################################  =>  Timer

def time():
    global timeleft,score,missed

    if(timeleft >= 12):
        pass
    else:
        timenumberlabel.configure(fg='red')

    if (timeleft >0):
        timeleft -=1
        timenumberlabel.configure(text=timeleft)
        timenumberlabel.after(1000,time)
    else:
        hintlabel.configure(text="Hit = {} | Missed = {} | Total Score = {} " .format(score,missed,score-missed))
        rr = messagebox.askretrycancel('Notification',' For play Again Hit Retry Button')
        if(rr==True):
            score=0
            missed=0
            timeleft=60
            timenumberlabel.configure(text=timeleft)
            midelfontlabel.configure(text=words[0])
            scorenumberlabel.configure(text=score)


#############################################################  =>  variables
score=0
missed=0
timeleft=60
count=0
wordslider=''


#############################################################  =>  label
topfontlabel = Label(screen,text='',fg='red',bg="powder blue",font=('arial',25,'italic bold'),width=40)
topfontlabel.place(x=10,y=40)
labelslider()

random.shuffle(words)
midelfontlabel = Label(screen,text=words[0],bg="powder blue",font=('arial',25,'italic bold'))
midelfontlabel.place(x=330,y=280)

scoretextlabel = Label(screen,text="Your score is: ",bg="powder blue",font=('arial',25,'italic bold'),fg="blue")
scoretextlabel.place(x=50,y=120)

scorenumberlabel = Label(screen,text=score,bg="powder blue",font=('arial',20,'italic bold'),fg="blue")
scorenumberlabel.place(x=130,y=170)

timetextlabel = Label(screen,text="Time left: ",bg="powder blue",font=('arial',25,'italic bold'),fg="blue")
timetextlabel.place(x=570,y=120)

timenumberlabel = Label(screen,text=timeleft,bg="powder blue",font=('arial',20,'italic bold'),fg="blue")
timenumberlabel.place(x=620,y=170)

hintlabel = Label(screen,text=" Type the given word and hit Enter ",bg="powder blue",font=('arial',25,'italic bold'),fg="gray")
hintlabel.place(x=140,y=430)


############################################################   =>  Input Entry
Input = Entry(screen,font=('arial',18,'italic bold'),bd=8,justify=CENTER)
Input.place(x=250,y=335)
Input.focus_set()


#############################################################  =>  match word

screen.bind('<Return>',matchword)

screen.mainloop()