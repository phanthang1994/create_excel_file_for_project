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
output_path = 'UPDDATE_MANY_CHU_DE.xlsx'
workbook = xlsxwriter.Workbook(output_path)
worksheet = workbook.add_worksheet()

# Add headers
worksheet.write('A1', 'id')
worksheet.write('B1', 'chu_de_name')
worksheet.write('C1', 'image')
worksheet.write('D1', 'so_nguoi_theo_hoc')
worksheet.write('E1', 'category_id')
worksheet.write('F1', 'description')
worksheet.write('G1', 'youtube_code')


# Loop through the files and extract name and extension
for row_num, file in enumerate(files, start=1):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        filename, extension = os.path.splitext(file)

        # Construct the new filename using formatted datetime
        worksheet.write(row_num, 1, filename)
        worksheet.write(row_num, 2, f"chu_de-{filename}-{formatted_datetime}{extension}")
        worksheet.write(row_num, 3, random.randint(30001, 100000))
        worksheet.write(row_num, 4, 9)
        new_filename = f"chu_de-{filename}-{formatted_datetime}{extension}"
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(file_path, new_file_path)

# Save the workbook
workbook.close()

print(f"File names and information saved to {output_path}")

