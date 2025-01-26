from openpyxl import load_workbook, Workbook
from openpyxl.utils import get_column_letter
wb = Workbook()
ws = wb.active
ws.title = "Data"
ws.append(['Suneel', 'is', 'Great'])
ws.append(['Vinod', 'is', 'Great'])
ws.append(['Pavan', 'is', 'Great'])
ws.append(['Kranthi', 'is', 'Great'])
wb.save('Suneel.xlsx')

