import xlsxwriter as tb
w=tb.Workbook("E:\\Old_practice\\jag1.xlsx")
w1=w.add_worksheet("my")
w1.write("A1","Name")
w1.write("B1","roll no")
w1.write("C1","Address")

b=["ram","sham","sita"]
c=[31,32,33]
d=["aa12","aa13","aa14"]
for i in range(len(b)):
    w1.write(i+1,0,b[i])
    w1.write(i+1,1,c[i])
    w1.write(i+1,2,d[i])

w1.write_formula("b6","=sum(b2:b4")




w.close()

