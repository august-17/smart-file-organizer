import os
import tkinter as tk
from tkinter import filedialog
import shutil

root = tk.Tk()                                          # Create the root window
root.withdraw()                                         # Hide the root window

folder_path = filedialog.askdirectory()                 # Open a dialog to select a folder and store its path

if not folder_path:
    
    print("No folder selected.")
    exit()


if not os.listdir(folder_path):
    print("Selected folder is empty.")
    exit()

print("Selected:", folder_path)
print("Organizing files...")
print()

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif"],
    "Documents": [".pdf", ".txt", ".docx", ".doc", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Others": []
}

for category in file_types:

    folder_to_create = os.path.join(folder_path, category)

    if not os.path.exists(folder_to_create):

        os.mkdir(folder_to_create)

files_moved = 0

for item in os.listdir(folder_path):
    
    item_path = os.path.join(folder_path, item)         # Create the complete path of the current item

    if os.path.isfile(item_path):
        
        file_name, extension = os.path.splitext(item)
        extension = extension.lower()
        category = "Others"

        for folder_name, extensions in file_types.items():
        
            if extension in extensions:
               category = folder_name
               break

        destination_folder = os.path.join(folder_path, category)
        destination_path = os.path.join(destination_folder, item)
        
        counter = 1
        renamed = False

        while os.path.exists(destination_path):

            renamed = True

            print("File already exists:", os.path.basename(destination_path))

            new_name = f"{file_name}_{counter}{extension}"
            destination_path = os.path.join(destination_folder, new_name)

            print("Trying:", new_name)
            counter += 1

        print()

        if renamed:
            print(f"\nRenamed: {item} -> {os.path.basename(destination_path)}")


        try:
            shutil.move(item_path, destination_path)
            files_moved += 1

        except Exception as e:
            print(f"Error moving {item}: {e}")


print(f"\nOrganization complete! {files_moved} file(s) moved.")