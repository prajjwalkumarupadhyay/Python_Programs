subjects=['English','Hindi','Maths','Science','Social Science']
marks=0
for i in subjects:
    mark=int(input(f'Enter Your Marks in {i}\n'))
    marks+=mark
percentage=(marks/500)*100
print('Your Total Marks is :',marks)
print('Your percentage is :',percentage)
