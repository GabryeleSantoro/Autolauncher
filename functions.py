import psutil
import os
from languages import getText
import win32con as wcon
from win32api import GetLogicalDriveStrings
from win32file import GetDriveType

def get_drives_list(drive_types=(wcon.DRIVE_REMOVABLE,)):
    drives_str = GetLogicalDriveStrings()
    drives = (item for item in drives_str.split("\x00") if item)
    return [item[:2] for item in drives if not drive_types or GetDriveType(item) in drive_types]

def printDisks():
   drive_filters_examples = (
        (None, "All"),
        ((wcon.DRIVE_REMOVABLE,), "Removable"),
        ((wcon.DRIVE_FIXED, wcon.DRIVE_CDROM), "Fixed and CDROM"),
    )
   for drive_types_tuple, display_text in drive_filters_examples:
        drives = get_drives_list(drive_types=drive_types_tuple)
        print("{:s} drives:".format(display_text))
        for drive in drives:
            print("{:s}  ".format(drive), end="")
        print("\n")

def find_files(filename, search_path):
   result = []

   for root, dir, files in os.walk(search_path):
      print(root, dir, files)
      if filename in files:
         result.append(os.path.join(root, filename))
   return result
       

def getDisks():
   return psutil.disk_partitions()
   