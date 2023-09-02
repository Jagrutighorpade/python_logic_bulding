import xlsxwriter as df
w=df.Workbook("E:\\Old_practice\\jag2.xlsx")
w1=w.add_worksheet("hey")
w1.write("A1","Name")
w1.write("B1","Roll no")
w.close()