import random
import os
import xlsxwriter
from datetime import datetime
import shutil  # Import the shutil module for file operations

# Create a new Excel workbook and add a worksheet
output_path = 'update_many_chu_de.xlsx'
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

# Get the current datetime
current_datetime = datetime.now()

# Format the datetime as "ddmmyyhms"
formatted_datetime = current_datetime.strftime('%d%m%y%H%M%S')

# Folder paths
source_folder_path = './lesson_'
destination_folder_path = f'./new_lesson_update{formatted_datetime}'

# Create the new folder if it doesn't exist
if not os.path.exists(destination_folder_path):
    os.makedirs(destination_folder_path)



# List all files in the source directory
files = os.listdir(source_folder_path)

# Loop through the files and extract name and extension
for row_num, file in enumerate(files, start=1):
    file_path = os.path.join(source_folder_path, file)
    if os.path.isfile(file_path):
        filename, extension = os.path.splitext(file)

        # Construct the new filename using formatted datetime
        worksheet.write(row_num, 1, filename)
        new_filename = f"chu_de-{filename}-{formatted_datetime}{extension}"

        # Copy the image to the destination folder with the new filename
        new_file_path = os.path.join(destination_folder_path, new_filename)
        shutil.copy(file_path, new_file_path)

        worksheet.write(row_num, 2, new_filename)
        worksheet.write(row_num, 3, random.randint(30001, 100000))
        worksheet.write(row_num, 4, 'Null')
        worksheet.write(row_num, 5, 'Null')
        worksheet.write(row_num, 6, 'Null')
        worksheet.write(row_num, 7, 'Null')

# Save the workbook
workbook.close()

print(f"File names and information saved to {output_path}")
