import psutil
import os
from languages import getText
from tkinter import messagebox

def find_files(filename, search_path):
   result = []

   for root, dir, files in os.walk(search_path):
      print(root, dir, files)
      if filename in files:
         result.append(os.path.join(root, filename))
   return result
       

def getDisks():
   return psutil.disk_partitions()
   