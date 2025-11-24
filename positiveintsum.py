#This Program sums the square of integer smaller than the entered input
num=int(input('Enter a Positive integer: '))
n=1
for i in range(2,num):
    n=n+i**2
    
print('The total sum is ',n)