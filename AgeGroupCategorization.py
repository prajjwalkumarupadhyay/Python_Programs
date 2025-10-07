#Age Group Categorization

print("Enter Your name and age and or type 'exit' to stop")

child=[]    # Creating Lists for Categorizing  peoples 
adult=[]
Teenagers=[]
senior=[]

while True:
    name=input("Tell me Your name\n") 
    if name.lower()=='exit':
     break
    age=int(input("How old are you\n")) 
    if age<13:
        print('You are a child')
        child.append(name)
    elif age>=13 and age<20:
        print('You are a Teenager')
        Teenagers.append(name)
    elif age>=20 and age<60:
        print('You are an adult')
        adult.append(name)
    elif age>=60:
        print('You are a senior citizen')
        senior.append(name)

print('\n Summary')
print('Children',child)
print('Teenagers',Teenagers)
print('Adults',adult)
print('Senior',senior)