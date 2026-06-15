import os
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil



file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif"],
    "Documents": [".pdf", ".txt", ".docx", ".doc", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Others": []
}



def create_category_folders(folder_path):

    # Create category folders if they don't exist
    for category in file_types:

        folder_to_create = os.path.join(folder_path, category)

        if not os.path.exists(folder_to_create):

            os.mkdir(folder_to_create)



def get_category(extension):

    category = "Others"

    # Find the category that matches the file extension
    for folder_name, extensions in file_types.items():

        if extension in extensions:
            category = folder_name
            break

    return category



def get_unique_destination(destination_folder, file_name, extension, item):

    destination_path = os.path.join(destination_folder, item)                   # Create the complete path of the destination file

    counter = 1
    renamed = False
    messages = []

    # Generate a new filename if a file with the same name already exists in the destination folder
    while os.path.exists(destination_path):

        renamed = True
        messages.append(
            f"File already exists: {os.path.basename(destination_path)}"
        )

        new_name = f"{file_name}_{counter}{extension}"
        destination_path = os.path.join(destination_folder, new_name)

        messages.append(
            f"Trying: {new_name}"
        )
        print()

        counter += 1

    return destination_path, renamed, messages



def create_summary(category_count, files_moved):

    summary = "Organization complete!\n\n"                          # Create a summary of the organization results

    for category, count in category_count.items():

        if count > 0:
            summary += f"{category}: {count}\n"

    summary += f"\nTotal: {files_moved} file(s) moved."

    return summary



def main():

    root = tk.Tk()                                          # Create the root window
    root.withdraw()                                         # Hide the root window

    folder_path = filedialog.askdirectory()                 # Open a dialog to select a folder and store its path



    if not folder_path:
        messagebox.showwarning(                             # Display a warning if no folder was selected
            "Smart File Organizer",
            "No folder selected."
        )
        exit()

    if not os.listdir(folder_path):
        messagebox.showinfo(                                # Display an info message if the selected folder is empty   
            "Smart File Organizer",
            "Selected folder is empty."
        )
        exit()

    print("Selected:", folder_path)
    print("Organizing files...")
    print()



    #Create category folders before moving files
    create_category_folders(folder_path)

    files_moved = 0
    category_count = {}
    category_count = {
        category: 0
        for category in file_types
    }



    for item in os.listdir(folder_path):
    
        item_path = os.path.join(folder_path, item)                 # Create the complete path of the current item

        if os.path.isfile(item_path):
        
            file_name, extension = os.path.splitext(item)           # Split the filename into name and extension
            extension = extension.lower()
        
            category = get_category(extension)                      # Get the category for the file based on its extension

            destination_folder = os.path.join(folder_path, category)

            destination_path, renamed, messages = get_unique_destination(
                destination_folder,
                file_name,
                extension,
                item
            )

            for message in messages:
                print(message)

            if messages:
                print()

            if renamed:                                             # Display the final renamed filename if a duplicate was found
            
                print(f"Renamed: {item} -> {os.path.basename(destination_path)}")
                print()

            try:                                                    # Move the file and continue even if one file causes an error
                shutil.move(item_path, destination_path)
                
                files_moved += 1
                category_count[category] += 1

            except Exception as e:
                print(f"Error moving {item}: {e}")



    summary = create_summary(
        category_count,
        files_moved
    )

    print("\n" + summary)

    messagebox.showinfo(                                            # Display the summary in a message box
        "Smart File Organizer",
        summary
    )



if __name__ == "__main__":
    main()