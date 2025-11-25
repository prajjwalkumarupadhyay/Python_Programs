num=input('Enter two number separated by space: ')
num1=int(num.split()[0])
num2=int(num.split()[1])
while num2!=0:
    t=num2
    num2=num1%num2
    num1=t
print('num1=',num1,'num2 = ',num2)