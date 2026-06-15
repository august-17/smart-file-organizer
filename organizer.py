import os
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
import shutil

LOG_FILE_PREFIX = "organizer_log_"

MULTI_EXTENSIONS = [".tar.gz", ".tar.bz2", ".tar.xz"]



def create_hidden_root():

    root = tk.Tk()                          # Create the root window
    root.withdraw()                         # Hide the root window

    return root


file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif"],
    "Documents": [".pdf", ".txt", ".docx", ".doc", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".tar.gz", ".tar.bz2", ".tar.xz"],
    "Code": [".py", ".java", ".class", ".cpp", ".hpp", ".c", ".h", ".js", ".jsx", ".html", ".css", ".json", ".xml", ".yml", ".yaml", ".ts", ".tsx", ".go", ".rb", ".php", ".jar", ".ipynb", ".mat", ".sql", ".r", ".swift", ".cs", ".rs", ".kt", ".scala", ".lua", ".vue"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".app", ".apk", ".dmg", ".cmd", ".com", ".bin"],
    "Others": []
}



def create_category_folders(folder_path, file_types):

    # Create category folders if they don't exist
    for category in file_types:

        folder_to_create = os.path.join(folder_path, category)

        if not os.path.exists(folder_to_create):

            os.mkdir(folder_to_create)



def initialize_category_count(file_types):

    return {
        category: 0
        for category in file_types
    }



def get_category(extension, file_types):

    category = "Others"

    # Find the category that matches the file extension
    for folder_name, extensions in file_types.items():

        if extension in extensions:
            category = folder_name
            break

    return category



def get_file_extension(filename):

    lower_filename = filename.lower()

    for extension in MULTI_EXTENSIONS:

        if lower_filename.endswith(extension):

            file_name = filename[:-len(extension)]

            return file_name, extension

    return os.path.splitext(filename)



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

        counter += 1

    return destination_path, renamed, messages


def print_messages(messages):

    for message in messages:
        print(message)

    if messages:
        print()



def organize_files(folder_path, file_types):

    files_moved = 0
    category_count = initialize_category_count(file_types)
    log_entries = []


    for item in os.listdir(folder_path):

        # Skip organizer log files
        if item.startswith(LOG_FILE_PREFIX):
            continue
    
        item_path = os.path.join(folder_path, item)                             # Create the complete path of the current item

        if os.path.isfile(item_path):
        
            file_name, extension = get_file_extension(item)                     # Split the filename into name and extension
            extension = extension.lower()
        
            category = get_category(extension, file_types)                      # Get the category for the file based on its extension

            destination_folder = os.path.join(folder_path, category)

            destination_path, renamed, messages = get_unique_destination(
                destination_folder,
                file_name,
                extension,
                item
            )

            print_messages(messages)

            if renamed:                                             # Display the final renamed filename if a duplicate was found
            
                print(f"Renamed: {item} -> {os.path.basename(destination_path)}")
                print()

                log_entries.append(
                    f"Renamed: {item} -> {os.path.basename(destination_path)}"
                )

            try:                                                    # Move the file and continue even if one file causes an error
                shutil.move(item_path, destination_path)

                files_moved += 1
                category_count[category] += 1

                log_entries.append(
                    f"Moved: {os.path.basename(destination_path)} -> {category}"
                )

            except Exception as e:
                print(f"Error moving {item}: {e}")

                log_entries.append(
                    f"Error moving {item}: {e}"
                )

    return files_moved, category_count, log_entries



def create_summary(category_count, files_moved):

    summary = "Organization complete!\n\n"                          # Create a summary of the organization results

    for category, count in category_count.items():

        if count > 0:
            summary += f"{category}: {count}\n"

    summary += f"\nTotal: {files_moved} file(s) moved."

    return summary



def write_log_file(folder_path, log_entries, summary):

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    log_path = os.path.join(
        folder_path,
        f"{LOG_FILE_PREFIX}{timestamp}.txt"
    )

    with open(log_path, "w", encoding="utf-8") as log_file:

        log_file.write("Smart File Organizer Log\n")
        log_file.write("=" * 30 + "\n\n")

        for entry in log_entries:
            log_file.write(entry + "\n")

        log_file.write("\n")
        log_file.write(summary)



def main():

    create_hidden_root()

    folder_path = filedialog.askdirectory()                 # Open a dialog to select a folder and store its path


    if not folder_path:
        messagebox.showwarning(                             # Display a warning if no folder was selected
            "Smart File Organizer",
            "No folder selected."
        )
        return

    if not os.listdir(folder_path):
        messagebox.showinfo(                                # Display an info message if the selected folder is empty   
            "Smart File Organizer",
            "Selected folder is empty."
        )
        return

    print("Selected:", folder_path)
    print("Organizing files...")
    print()


    # Create category folders before moving files
    create_category_folders(folder_path, file_types)

    files_moved, category_count, log_entries = organize_files(folder_path, file_types)

    if files_moved == 0:
        message = "No files found to organize."
        print("\n" + message)

        messagebox.showinfo(
            "Smart File Organizer",
            message
        )
        return
    

    summary = create_summary(
        category_count,
        files_moved
    )

    write_log_file(
        folder_path,
        log_entries,
        summary
    )
    
    print("\n" + summary)

    messagebox.showinfo(                                            # Display the summary in a message box
        "Smart File Organizer",
        summary
    )



if __name__ == "__main__":
    main()