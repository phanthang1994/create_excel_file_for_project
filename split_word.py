import csv

# Specify the path to your CSV file
csv_file_path = 'phien_am.csv'

# Specify the file's encoding as 'utf-8'
file_encoding = 'utf-8'
split_results = []
# Use the 'with' statement to open the file and read its contents
with open(csv_file_path, 'r', encoding=file_encoding, newline='') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Each 'row' variable contains a list of values from a row in the CSV
        # You can access individual values by index, e.g., row[0], row[1], etc.
        for row in csv_reader:
            # Check if the row has at least one element
            if row:
                # Split the first column (row[0]) by ':'
                split_result = row[0].split(':')

                # Append the first part of the split string to the list
                if split_result:
                    split_results.append([split_result[-1]])

# Specify the path for the output CSV file
output_csv_file_path = 'phien_am_file.csv'

# Use the 'with' statement to open the output CSV file and write the split results
with open(output_csv_file_path, 'w', encoding=file_encoding, newline='') as output_csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(output_csv_file)

    # Write the split results to the output CSV file
    csv_writer.writerows(split_results)