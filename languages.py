import locale

language = "en_US"

def defineLanguage():
    setLanguage(locale.getlocale()[0])
    return locale.getlocale()

def getLanguage():
    return language

def setLanguage(var):
    global language
    language = var

def getText(index):
    path = "./languages/"+language+".txt"
    f = open(path, "r")
    content = f.readlines()
    return content[index]
