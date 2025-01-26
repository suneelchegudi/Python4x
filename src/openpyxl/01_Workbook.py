from openpyxl import load_workbook, Workbook

wb = load_workbook(r"D:\Python4x\Grades.xlsx")
ws = wb.active
print(ws)
print(ws['A1'].value)
ws['A1'].value = 'YourName'
wb.save(r"D:\Python4x\Grades.xlsx")
print(wb['Sheet2'])
wb.create_sheet('Suneel')
wb.save(r"D:\Python4x\Grades.xlsx")