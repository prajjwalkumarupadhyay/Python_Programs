#calculator
import sys
while True:
    print('''Select a serial no from the following options based on the Arthmetic operation you want to perform
          1. Addition
          2. Substraction
          3. Multiplication
          4. Division
          5. Exit''')
    enter=int(input())
    def Addition(a,b):
        return a+b
    def Multiplication(c,d):
        return c*d
    def Substraction(e,f):
        return e-f
    def Division(g,h):
        return g/h
    
    if enter==1:
        a=int(input('Enter the first number:\n'))
        b=int(input('Enter the second number:\n'))
        sum=Addition(a,b)
        print('Sum:',sum)
        data=input('Do you want to continue, type yes;\n')
        if data.lower()=='yes':
            continue
        else:
            sys.exit('Thank You !')
    if enter==3:
        c=int(input('Enter the first number:\n'))
        d=int(input('Enter the second number:\n'))
        Product=Multiplication(c,d)
        print('Product:', Product)
        data=input('Do you want to continue, type yes:\n')
        if data.lower()=='yes':
            continue
        else:
            sys.exit('Thank You !')
    if enter==2:
        e=int(input('Enter the first number:\n'))
        f=int(input('Enter the second number:\n'))
        difference=Substraction(e,f)
        print('Difference:',difference)
        data=input('Do you want to continue, type yes:\n')
        if data.lower()=='yes':
            continue
        else:
            sys.exit('Thank You !')
    if enter==4:
        g=int(input('Enter the first number:\n'))
        h=int(input('Enter the second number:\n'))
        div=Division(g,h)
        print('Division:',div)
        data=input('Do you want to continue, type yes:\n')
        if data.lower()=='yes':
            continue
        else:
            sys.exit('Thank You !')
    if enter==5:
        print('Thank You!')
        sys.exit()