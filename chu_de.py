import random
import shutil

folder_path = './lesson_'

import os
import xlsxwriter
from datetime import datetime

# Get the current datetime
current_datetime = datetime.now()

# Format the datetime as "ddmmyyhms"
formatted_datetime = current_datetime.strftime('%d%m%y%H%M%S')
destination_folder_path = f'./new_lesson{formatted_datetime}'

# Create the new folder if it doesn't exist
if not os.path.exists(destination_folder_path):
    os.makedirs(destination_folder_path)

# List all files in the directory
files = os.listdir(folder_path)

# Create a new Excel workbook and add a worksheet
output_path = 'chu_de_create.xlsx'
workbook = xlsxwriter.Workbook(output_path)
worksheet = workbook.add_worksheet()

# Add headers
worksheet.write('A1', 'chu_de_name')
worksheet.write('B1', 'image')
worksheet.write('C1', 'so_nguoi_theo_hoc')
worksheet.write('D1', 'category_id')
worksheet.write('E1', 'description')
worksheet.write('F1', 'youtube_code')


# Loop through the files and extract name and extension
for row_num, file in enumerate(files, start=1):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        filename, extension = os.path.splitext(file)

        # Construct the new filename using formatted datetime
        worksheet.write(row_num, 0, filename)
        worksheet.write(row_num, 1, f"chu_de-{filename}-{formatted_datetime}{extension}")
        worksheet.write(row_num, 2, random.randint(30001, 100000))
        new_filename = f"chu_de-{filename}-{formatted_datetime}{extension}"
        # Copy the image to the destination folder with the new filename
        new_file_path = os.path.join(destination_folder_path, new_filename)
        shutil.copy(file_path, new_file_path)

# Save the workbook
workbook.close()

print(f"File names and information saved to {output_path}")

