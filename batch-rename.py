# Microsoft CMT File Renamer
# This Python script is specifically written for submission files downloaded from Microsoft CMT. 
# It renames the files and puts them in the root folder.
# Usage: 1. Download the submissions from Microsoft CMT
#        2. Extract the zip file to a folder (such as C:\Users\Sajid\Downloads\Submissions)
#        3. Copy the path of the folder and change it in the root_folder_path variable
#        4. Execute the script.

import os
import shutil

# Function to rename PDF files in "Submission" subfolders

def rename_pdfs(root_folder):
    i = 0
    for foldername, subfolders, filenames in os.walk(root_folder):
        if os.path.basename(foldername) == "Submission":
            # Assuming there is only one PDF file in each "Submission" subfolder
            pdf_file = next((file for file in filenames if file.endswith(".pdf")), None)
            if pdf_file:
                pdf_path = os.path.join(foldername, pdf_file)
                new_name = os.path.basename(os.path.dirname(foldername)).zfill(3) + ".pdf"
                new_path = os.path.join(root_folder, new_name)

                os.rename(pdf_path, new_path)
                print(f'Renamed: {pdf_path} to {new_path}')

# Replace 'path_to_your_root_folder' with the actual path to your root folder
root_folder_path = r'C:\Users\Sajid\Downloads\Submissions'
print(root_folder_path)
rename_pdfs(root_folder_path)
print('finish')
