# Microsoft CMT File Renamer
# This Python script is specifically written for camera ready files downloaded from Microsoft CMT. It renames the files and puts them in the root folder.

import os
import shutil

# Function to rename PDF files in "Submission" subfolders
import os
import shutil

def rename_largest_pdf(root_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        if os.path.basename(foldername) == "CameraReady":
            # Assuming there is at least one PDF file in each "CameraReady" subfolder
            pdf_files = [file for file in filenames if file.endswith(".pdf")]

            if pdf_files:
                # Find the largest PDF file
                largest_pdf = max(pdf_files, key=lambda x: os.path.getsize(os.path.join(foldername, x)))

                pdf_path = os.path.join(foldername, largest_pdf)
                new_name = os.path.basename(os.path.dirname(foldername)).zfill(3) + ".pdf"
                new_path = os.path.join(root_folder, new_name)

                # Use shutil.move to handle overwriting if the file already exists
                shutil.move(pdf_path, new_path)
                print(f'Renamed and overwritten if exists: {pdf_path} to {new_path}')
                break  # Stop after renaming the largest file in the first "CameraReady" subfolder

# Replace 'path_to_your_root_folder' with the actual path to your root folder
root_folder_path = r'C:\Users\Sajid\Downloads\CameraReadys2-172'
print(root_folder_path)
rename_largest_pdf(root_folder_path)
print('finish')
