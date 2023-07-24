import os

import win32con as wcon
from win32api import GetLogicalDriveStrings
from win32file import GetDriveType

def find_file(root_folder, rex):
    
   results = []
    
   for root,dirs,files in os.walk(root_folder):
      for f in files:
         result = rex.search(f)
         if result:
            results.append(os.path.join(root, f))
   return results
       

def getDisks(drive_types=(wcon.DRIVE_CDROM,wcon.DRIVE_REMOVABLE)):
    drives_str = GetLogicalDriveStrings()
    drives = (item for item in drives_str.split("\x00") if item)
    print(drives)
    return [item[:2] for item in drives if not drive_types or GetDriveType(item) in drive_types]
   