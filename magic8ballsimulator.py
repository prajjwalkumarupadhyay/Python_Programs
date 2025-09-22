#This is Magic 8 ball simulator 
import random
response=random.randint(1,8)

question=input()

if response==1:
    print('No')
elif response==2:
    print('Yes')
elif response==3:
    print('Hell No')
elif response==4:
    print('dammit')
elif response==5:
    print('Never')
elif response==6:
    print('Maybe')
elif response==7:
    print('Definitely ')
else:
    print('Sure')


print('I hope you enjoyed it')

