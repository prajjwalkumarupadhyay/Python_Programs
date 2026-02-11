# Area of Traingle using herons formula 
a=float(input('Enter the first side of traingle:\n'))
b=float(input('Enter the seconde side of traingle:\n'))
c=float(input('Enter the third side of traingle:\n'))
print(a,b,c)
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(' area of traingle :',area)