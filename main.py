from tkinter import *
from functions import *
from languages import *

root = Tk()
root.title("Autorun Launcher")
root.geometry( "500x200" )

language,label,button,clicked = None,None,None,None

setLanguage(defineLanguage()[0])

#Language
languages = [
   "it_IT",
   "en_US"
]

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
        messagebox.showinfo(getText(2),getText(2))
    else:
        messagebox.showerror(getText(3), getText(4))

def generateUI():

    global language
    language = StringVar()
    language.set( getLanguage() )
    language.trace("w", optionChanged)
    drop2 = OptionMenu( root , language , *languages )

    #Title
    global label
    label = Label(root, text = getText(0), font=('Helvetica 15 bold'))

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
    button = Button( root , text = getText(1) , command = lambda : searchAutorun(clicked.get()) )

    #Layout
    root.grid_columnconfigure(0, weight=1)

    label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky="ew")
    drop2.grid(row = 0, column = 0, padx = 10, pady = 10, sticky="e")

    drop.grid(row = 2, column = 0, padx = 10, pady = 10)
    button.grid(row = 3, column = 0, padx = 10, pady = 10)

    root.mainloop()

generateUI()