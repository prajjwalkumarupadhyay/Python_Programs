#This program will represnet you marks in each subject

subjects=['English','Hindi','Maths','Science','Social Science']
marks={}

for subject in subjects:
    mark=int(input(f'Enter Your  marks in {subject}\n'))
    marks[subject]=mark

print("Marks Entered: ",marks)