from openpyxl import  load_workbook,workbook

wb = load_workbook("Grades.xlsx")
ws = wb.active
print(ws['D5'].value)
value_range = ws['A2': 'D6']
print(value_range)
for a, b , c, d in value_range:
    print(a.value,b.value,c.value,d.value)

