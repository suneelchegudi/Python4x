from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

wb = load_workbook(r"D:\Python4x\Grades.xlsx")
ws = wb['Sheet2']

for row in range(1, 11):
    for col in range(1,5):
        char = get_column_letter(col)
        print(ws[char+str(row)].value)
        # ws[char + str(row)] = char+str(row)
wb.save(r"D:\Python4x\Grades.xlsx")


