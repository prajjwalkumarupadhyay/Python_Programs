#This program can check if n is a multiple of m
def is_multiple(n,m):
        if n%m==0:
          print(f'{n} is a multiple of {m} ')
        else:
           print(f'{n} is not a multiple of {m}')

m=int(input('Enter the desired number :'))
n=int(input('Enter the number which you want to check :'))
is_multiple(n,m)


