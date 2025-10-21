#Through this Program you can find factorial of any number 

num=int(input('Enter the number of which you want to know factorial\n'))
fact=1
for x in range (2,num+1):
    fact=fact*x

print(fact)
