import csv
examplefile=open('example.csv')
exampledata=csv.reader(examplefile)
list1=list(exampledata)
print(list1)
print(list1[3][3])
print()
examplefile=open('example.csv')
exampledata=csv.reader(examplefile)
for row in exampledata:
    print('Row #'+str(exampledata.line_num)+' '+str(row))



