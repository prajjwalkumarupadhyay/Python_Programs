#This program will tell you the power of desired number
number=[]
n=int(input('Enter the number whose power you want to know: '))
power=int(input('Input at which power you want to know the values: '))
for i in range(0,power+1):
    number.append(n**i)
    
print(number)