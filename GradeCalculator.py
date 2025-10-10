#This program categorize students on the bases of there grades
GradeA_plus_students=[]
GradeA_students=[]
GradeB_plus_students=[]
GradeB_students=[]
GradeC_students=[]
GradeD_students=[]
Fail_students=[]

while True:
    print("Enter the name of the student or type 'exit' to end the program." )
    name=input()
    if name=='exit':
        break
    subjects=['English','Hindi','Maths','Science','Social Science']
    Total_marks=0
    for subject in subjects:
        mark=int(input(f'Enter Marks in {subject}\n'))
        Total_marks+=mark
    percentage=(Total_marks/500)*100
    
    if percentage>=80:
        print('Performance Level: Exceptional mastery and innovative thinking')
        GradeA_plus_students.append(name)
    elif percentage>=70:
        print('Performance Level: Strong grasp with minor areas for improvement')
        GradeA_students.append(name)
    elif percentage>=60:
        print('Performance Level: Above-average understanding and application')
        GradeB_plus_students.append(name)
    elif percentage>=50:
        print('Performance Level: Solid performance with room for growth')
        GradeB_students.append(name)
    elif percentage>=40:
        print('Performance Level: Basic understanding; needs improvement')
        GradeC_students.append(name)
    elif percentage>=35:
        print('Performance Level: Barely meets minimum standards')
        GradeD_students.append(name)
    elif percentage<35:
        print('Performance Level: Unsatisfactory; must retake the course')
        Fail_students.append(name)

print('Students categories based on their performamce')
print('Grade A+ students:',GradeA_plus_students)
print('Grade A students:',GradeA_students)
print('Grade B+ students:',GradeB_plus_students)
print('Grade B students:',GradeB_students)
print('Grade C students:',GradeC_students)
print('Grade D students:',GradeD_students)
print('Failed Students:',Fail_students)

