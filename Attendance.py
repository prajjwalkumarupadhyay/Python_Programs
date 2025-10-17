#You can calculate your attendance throught this
attended_lectures=int(input('Enter your total attended lectures\n'))
scheduled_classes=int(input('Total no of classes scheduled\n'))
print('Mark your attendance')
lectures={'monday':5,'tuesday':6,'wednesday':4,'thursday':6,'friday':5,'saturday':5}
class_attended=0
print('Enter on which day you were present or type \'exit\' to end')
while True:
    present=input()
    if present.lower()=='exit':
        break
    if present.lower()=='monday':
        class_attended+=lectures.get(present)
    elif present.lower()=='tuesday':
        class_attended+=lectures.get(present)
    elif present.lower()=='wednesday':
        class_attended+=lectures.get(present)
    elif present.lower()=='thursday':
        class_attended+=lectures.get(present)
    elif present.lower()=='friday':
        class_attended+=lectures.get(present)
    elif present.lower()=='saturday':
        class_attended+=lectures.get(present)
    else:
        print('There is no such day ')
#For percentage Calculation
attendance=(class_attended+attended_lectures)/(scheduled_classes+31)
percentage=attendance*100
print('Classes you attended this week:',class_attended)
print('Attendance percentage:',percentage)
if percentage<75:
    print('Your attendance is very low , try attending classes regularly otherwise you will be detained')