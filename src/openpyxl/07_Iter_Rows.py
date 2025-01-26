from openpyxl import load_workbook

wb = load_workbook("Grades.xlsx")
ws = wb['Sheet1']


rows = ws.iter_rows( min_row= 1, max_row = 5, min_col = 1,max_col = 3)
print(rows)

Names = []
Subject1 = []
Subject2 = []
for a, b, c  in rows:

    Names.append(a.value)
    Subject1.append(b.value)
    Subject2.append(c.value)

print(Names)
print(Subject1)
print(Subject2)
