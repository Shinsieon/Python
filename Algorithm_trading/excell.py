import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.open('C:\\Users\\user\\Desktop\\kospi_stock_code.csv')
ws = wb.ActiveSheet
print(ws.Cells(1,1).Value)
excel.Quit()