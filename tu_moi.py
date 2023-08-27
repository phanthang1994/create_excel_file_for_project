import random

folder_path = './lesson'

import os
import xlsxwriter
from datetime import datetime

# Get the current datetime
current_datetime = datetime.now()

# Format the datetime as "ddmmyyhms"
formatted_datetime = current_datetime.strftime('%d%m%y%H%M%S')


# List all files in the directory
files = os.listdir(folder_path)

# Create a new Excel workbook and add a worksheet
output_path = 'tu_moi_info.xlsx'
workbook = xlsxwriter.Workbook(output_path)
worksheet = workbook.add_worksheet()

# Add headers
worksheet.write('A1', 'name')
worksheet.write('B1', 'image')
worksheet.write('C1', 'tu_loai')
worksheet.write('D1', 'phien_am')
worksheet.write('E1', 'vi_du')
worksheet.write('F1', 'audio')
worksheet.write('G1', 'che_tu')
worksheet.write('H1', 'cau_truc_cau')
worksheet.write('I1', 'chu_de_id')


# Loop through the files and extract name and extension
for row_num, file in enumerate(files, start=1):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        filename, extension = os.path.splitext(file)

        # Construct the new filename using formatted datetime
        worksheet.write(row_num, 0, filename)
        worksheet.write(row_num, 1, f"tu_moi-{filename}-{formatted_datetime}{extension}")
        worksheet.write(row_num, 8, 73)
        new_filename = f"tu_moi-{filename}-{formatted_datetime}{extension}"
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(file_path, new_file_path)

folder_path = './lesson_audio'
output_path = 'tu_moi_info.xlsx'

for row_num, file in enumerate(files, start=1):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        filename, extension = os.path.splitext(file)
        worksheet.write(row_num, 5, f"tu_moi-{filename}-{formatted_datetime}{extension}")
        new_filename = f"tu_moi-{filename}-{formatted_datetime}{extension}"
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(file_path, new_file_path)

# Save the workbook
workbook.close()

print(f"File names and information saved to {output_path}")

