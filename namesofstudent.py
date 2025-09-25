studentName=[]

while True:
    print('Enter the name of students '+ str(len(studentName)+1) +' ,else Type Nothing to stop:')
    name=input()
    if name=='Nothing':
        break
    studentName=studentName+[name]
print('The Names of the students are:')
for name in studentName:
    print(name)



