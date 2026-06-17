# Smart File Organizer

A Python desktop application that automatically organizes files into categorized folders based on their file extensions.

Built with Python and Tkinter, the application provides a graphical interface, progress tracking, duplicate-file handling, recursive folder organization, and detailed log generation for efficient file management.

---

## Features

### File Categorization
Automatically organizes files into folders such as:

- Images
- Documents
- Videos
- Audio
- Archives
- Code
- Executables
- Others

### Graphical User Interface
- Folder selection dialog
- Confirmation prompts
- Progress bar showing organization status
- Completion summary window

### Duplicate File Handling
If a file with the same name already exists in the destination folder, the application automatically renames the incoming file.

Example:

report.pdf  
report_1.pdf  
report_2.pdf

### Recursive Organization
Users can choose whether to organize:
- Only the selected folder
- The selected folder and all subfolders

### Activity Logging
Generates a timestamped log file containing:
- Files moved
- Renamed files
- Errors encountered
- Organization summary

Example:

organizer_log_2026-06-17_14-30-12.txt

### Multi-Extension Archive Support
Correctly identifies archive formats such as:

- .tar.gz
- .tar.bz2
- .tar.xz

### Error Handling
File movement operations are protected using exception handling so that one failed file does not stop the entire organization process.

---

## Supported File Categories

| Category | Examples |
|-----------|-----------|
| Images | .jpg, .jpeg, .png, .gif, .webp, .avif |
| Documents | .pdf, .txt, .docx, .doc, .xlsx, .ppt, .pptx, .csv |
| Videos | .mp4, .mkv, .avi, .mov, .webm |
| Audio | .mp3, .wav, .aac, .m4a, .aiff |
| Archives | .zip, .rar, .tar, .gz, .7z, .tar.gz, .tar.bz2, .tar.xz |
| Code | .py, .java, .cpp, .c, .js, .html, .css, .json, .sql and more |
| Executables | .exe, .msi, .bat, .sh, .apk, .dmg |
| Others | Uncategorized files |

---

## How It Works

1. Launch the application.
2. Select a folder to organize.
3. Choose whether subfolders should also be organized.
4. The application:
   - Creates category folders if needed.
   - Moves files into their respective folders.
   - Automatically resolves duplicate filenames.
   - Updates progress in real time.
5. A summary report and log file are generated upon completion.

---

## Requirements

- Python 3.8 or higher

No external libraries are required. The application uses only Python standard library modules.

---

## Running the Application

```bash
python organizer.py
```

---

## Example Folder Structure

### Before

```text
Downloads/
├── photo.jpg
├── report.pdf
├── song.mp3
├── archive.zip
└── script.py
```

### After

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Audio/
│   └── song.mp3
├── Archives/
│   └── archive.zip
├── Code/
│   └── script.py
└── organizer_log_2026-06-17.txt
```

---

## Technologies Used

- Python
- Tkinter
- os
- shutil
- datetime

---

## Future Improvements

- Drag-and-drop folder selection
- Custom file categories
- Undo last organization operation
- Dark mode support
- Standalone executable (.exe) release

---

## Author

**August Kumar Sasmal**

B.Tech Computer Science & Engineering  
Manipal Institute of Technology, Manipal