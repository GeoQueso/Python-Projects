#Get cell value from all sheets in a large workbook
#line 19 splits the output list into lists of ten values
#line 23-24 does the same thing as line 19.

import openpyxl

workbook = openpyxl.load_workbook('QuoteWorkbook.xlsx')

sheet = workbook.get_sheet_names()

lst = []

for sheet in workbook:
    if sheet['E10'].value not in lst:
        lst.append(sheet['E10'].value)

n=10

new_lst = [lst[i * n:(i + 1) * n] for i in range((len(lst) + n - 1) // n )]

new_list = []

#for i in range((len(lst) + n-1)//n):
    #new_list.append(lst[i*n:(i+1)*n])
for i in new_list:
    print (i)
