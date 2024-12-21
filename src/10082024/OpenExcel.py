import openpyxl
import os

# Define the path to the Excel file on your desktop
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
print(desktop_path)
file_name = 'test.xlsx'  # Replace with your Excel file name
file_path = os.path.join(desktop_path, file_name)
print(file_path)
# Load the workbook
try:
    wb = openpyxl.load_workbook(file_path)
    print(f"Successfully loaded {file_name}")
except FileNotFoundError:
    print(f"File {file_name} not found on the desktop.")
    exit()

# Select the active sheet
sheet = wb.active

# Print the values of the cells in the first sheet
for row in range(1, sheet.max_row + 1):
    for col in range(1, sheet.max_column + 1):
        cell = sheet.cell(row=row, column=col)
        print(f"Cell ({row}, {col}) value: {cell.value}")

# Save any changes (if you made any)
# wb.save(file_path)