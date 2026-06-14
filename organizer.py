import os

downloads_folder = os.path.expanduser("~/Downloads")

print("Downloads Folder:")
print(downloads_folder)

print("\nFiles in Downloads:")

for item in os.listdir(downloads_folder):
    print(item)