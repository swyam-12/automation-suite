import os
import shutil
from datetime import datetime

# Folder paths
source_folder = "test_folder"
destination_folder = "organized_files"

# Categories
categories = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Videos": [".mp4", ".avi"],
    "Music": [".mp3"],
}

# Create destination folders
for category in categories.keys():
    path = os.path.join(destination_folder, category)
    os.makedirs(path, exist_ok=True)

# Others folder
others_path = os.path.join(destination_folder, "Others")
os.makedirs(others_path, exist_ok=True)

# Organize files
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()
        moved = False

        for category, extensions in categories.items():
            if ext in extensions:
                dest_folder = os.path.join(destination_folder, category)
                dest_path = os.path.join(dest_folder, file)

                # Handle duplicate file names
                if os.path.exists(dest_path):
                    name, extn = os.path.splitext(file)
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                    new_name = f"{name}_{timestamp}{extn}"
                    dest_path = os.path.join(dest_folder, new_name)

                shutil.move(file_path, dest_path)
                print(f"Moved {file} → {category}")
                moved = True
                break

        if not moved:
            dest_path = os.path.join(others_path, file)
            shutil.move(file_path, dest_path)
            print(f"Moved {file} → Others")