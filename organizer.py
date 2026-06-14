import os

curr_folder = os.getcwd()

print("Current Folder:")
print(curr_folder)

print("\nFiles and Folders:")

for item in os.listdir(curr_folder):
    print(item)