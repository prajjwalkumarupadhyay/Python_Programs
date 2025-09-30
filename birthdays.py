#Birthdays of my Colleagues

Birthdays={'Krish':'28th Feb','Alfishan':'11th April','shyamant':'14th January','Ansh':'25th Jan','sheen':'11th Oct','keshav':'2nd Jan','Alquama':'20th April'}

while True:
    print('Enter the name:(blank to quit)')
    name=input()
    if name=='':
        break
    if name in Birthdays:
        print(Birthdays[name]+' is the birthday of '+name)
    else:
        print('I do not have birthday information for '+name)
        print('what is there birthday')
        bday=input()
        Birthdays[name]=bday
        print('database updated')