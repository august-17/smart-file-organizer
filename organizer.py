import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()                                      # Create the root window
root.withdraw()                                     # Hide the root window

folder_path = filedialog.askdirectory()             # Open a dialog to select a folder and store its path

if not folder_path:
    print("No folder selected.")
    exit()

print("Selected:", folder_path)

for item in os.listdir(folder_path):                # List all items in the selected folder

    item_path = os.path.join(folder_path, item)

    if os.path.isfile(item_path):
       
       file_name, extension = os.path.splitext(item)
       
       print("File Name:", file_name)
       print("Extension:", extension)
       print("-" * 25)

    else:
        print(item, "-> Folder")