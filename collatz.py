#This is collatz Program

x=int(input())
while x!=1:
    if x%2==0:
        x=x//2
        print(x)
    else:
        x=3*x+1
        print(x)

print(x)
