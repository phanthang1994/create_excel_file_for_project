import random
import os
import shutil

import xlsxwriter
from datetime import datetime

# Get the current datetime
current_datetime = datetime.now()

# Format the datetime as "ddmmyyhms"
formatted_datetime = current_datetime.strftime('%d%m%y%H%M%S')

# Folder paths
folder_path = './study_'
study_folder_path = f'./new_study_update{formatted_datetime}'
# Create the new folder if it doesn't exist
if not os.path.exists(study_folder_path):
    os.makedirs(study_folder_path)
# List all files in the directory
files = os.listdir(folder_path)

# Create a new Excel workbook and add a worksheet
output_path = 'tu_moi_updates.xlsx'
workbook = xlsxwriter.Workbook(output_path)
worksheet = workbook.add_worksheet()

# Add headers
worksheet.write('A1', 'id')
worksheet.write('B1', 'name')
worksheet.write('C1', 'image')
worksheet.write('D1', 'tu_loai')
worksheet.write('E1', 'phien_am')
worksheet.write('F1', 'vi_du')
worksheet.write('G1', 'audio')
worksheet.write('H1', 'che_tu')
worksheet.write('I1', 'cau_truc_cau')
worksheet.write('J1', 'chu_de_id')

# Loop through the files and extract name and extension
for row_num, file in enumerate(files, start=1):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        filename, extension = os.path.splitext(file)

        # Construct the new filename using formatted datetime
        worksheet.write(row_num, 1, filename)
        new_filename = f"tu_moi-{filename}-{formatted_datetime}{extension}"
        worksheet.write(row_num, 2, new_filename)
        worksheet.write(row_num, 3, 'Null')
        worksheet.write(row_num, 4, 'Null')
        worksheet.write(row_num, 5, 'Null')
        worksheet.write(row_num, 6, 'Null')
        worksheet.write(row_num, 7, 'Null')
        worksheet.write(row_num, 8, 'Null')
        worksheet.write(row_num, 9, 'Null')

        # Copy the image to the destination folder with the new filename
        new_file_path = os.path.join(study_folder_path, new_filename)
        shutil.copy(file_path, new_file_path)

# Loop through the audio files and update the worksheet
audio_folder_path = './audio_'
new_audio_folder_path = f'./new_audio_update{formatted_datetime}'
# Create the new folder if it doesn't exist
if not os.path.exists(new_audio_folder_path):
    os.makedirs(new_audio_folder_path)
audio_files = os.listdir(audio_folder_path)
for row_num, file in enumerate(audio_files, start=1):
    file_path = os.path.join(audio_folder_path, file)
    if os.path.isfile(file_path):
        filename, extension = os.path.splitext(file)
        new_filename = f"tu_moi-{filename}-{formatted_datetime}{extension}"
        worksheet.write(row_num, 6, new_filename)

        # Copy the image to the destination folder with the new filename
        new_file_path = os.path.join(new_audio_folder_path, new_filename)
        shutil.copy(file_path, new_file_path)

# Save the workbook
workbook.close()

print(f"File names and information saved to {output_path}")
