import locale
import ctypes

language = "en_US"

def defineLanguage():
    windll = ctypes.windll.kernel32
    windll.GetUserDefaultUILanguage()
    global language
    language = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

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
