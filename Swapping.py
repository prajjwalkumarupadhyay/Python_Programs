a=int(input('Enter a number:\n'))
b=int(input('Enter another number:\n'))
#Swapping Two numbers using a temporary variable
c=b
b=a
a=c
print('after swaping:')
print(a,b,sep=",")