import xlrd

rb = xlrd.open_workbook('text.xlsx')
sheet = rb.sheet_by_index(0)
val = sheet.row_values(0)[0]
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]


