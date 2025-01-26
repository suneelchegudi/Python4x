# Open existing workbook and load
import openpyxl

wb = openpyxl.load_workbook("Grades.xlsx")
wb.create_sheet("NewSheet",1)
wb.save("Grades.xlsx")