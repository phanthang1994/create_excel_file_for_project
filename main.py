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
output_path = 'filename_info.xlsx'
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
        new_filename = f"chu_de-{filename}-{formatted_datetime}{extension}"
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(file_path, new_file_path)
        worksheet.write(row_num, 0, filename)
        worksheet.write(row_num, 1, new_filename)
        worksheet.write(row_num, 2, random.randint(30001, 100000))


# Save the workbook
workbook.close()

print(f"File names and information saved to {output_path}")

