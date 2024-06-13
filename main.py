import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files(directory):
    # Dictionary to map file extensions to folder names
    file_types = {
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Video': ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Programs': ['.exe', '.bat', '.sh', '.py', '.js', '.html', '.css'],
        'Others': []
    }

    # Ensure all defined folders exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(directory, 'Others', filename))

    messagebox.showinfo("Success", "Files have been organized successfully.")

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        organize_files(directory)

# Create the main window
root = tk.Tk()
root.title("File Management System")

# Create a button to browse for the directory
browse_button = tk.Button(root, text="Select Folder", command=browse_directory)
browse_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
