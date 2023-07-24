from tkinter import *
from functions import *
from languages import *
from tkinter import messagebox

root = Tk()
root.title("Autorun Launcher")
root.geometry( "500x300" )

language,label,button,clicked,globalDisks = None,None,None,None,None

defineLanguage()

#Language
languages = [
   "it_IT",
   "en_US"
]

printDisks()

def refresh(self):
    self.destroy()
    self.__init__()

def optionChanged(*args):
    setLanguage(language.get())
    label.config(text = getText(0))
    button.config(text = getText(1))

def searchAutorun(path):
    print(path)
    temp = (find_files("autorun.inf",path))
    if len(temp) > 0:
        messagebox.showinfo(getText(3),getText(3))
    else:
        messagebox.showerror(getText(4), getText(5))

def generateUI():

    global language
    language = StringVar()
    language.set( getLanguage() )
    language.trace("w", optionChanged)
    drop2 = OptionMenu( root , language , *languages )

    #Title
    global label
    label = Label(root, text = getText(0), font=('Helvetica 15 bold'))

    global labelDisks
    labelDisks = Label(root,text = getText(1), font=('Helvetica 10 italic'))
    #Disks
    disks = getDisks()

    options = []

    for disk in disks:
        options.append(disk.device)

    global clicked
    clicked = StringVar()

    clicked.set( options[0] )
    drop = OptionMenu( root , clicked , *options )
    
    #Search Button
    global button
    button = Button( root , text = getText(2) , command = lambda : searchAutorun(clicked.get()) )

    #Layout
    root.grid_columnconfigure(0, weight=1)

    drop2.place(x = 400, y = 20)
    label.place(x = 100, y = 75)

    labelDisks.place(x = 150, y = 150)
    drop.place(x = 300, y = 145)

    button.place(x = 200, y = 220)

    

    root.mainloop()

generateUI()