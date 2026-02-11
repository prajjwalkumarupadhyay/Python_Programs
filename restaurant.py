#Restaurant bill Program
print('\nWelcome to our Restaurant,What would you like to  Order')
print()
print('MENU\n'.rjust(22,' '))
print('''\tfood\t\tPrice\n
        Pasta\t\t350\n
        Burger\t\t250\n
        Pizza\t\t450\n
        Momos\t\t150\n
        Fries\t\t170\n''')
menu={'pasta':350,'burger':250,'pizza':450,'momos':150,'fries':170}
bill=0
print(menu)
order_placed=[]
print('Order Your dish or type \'exit\' to end order')
while True:
    order=input()
    if order.lower()=='exit':
        break
    if order.lower()=='pasta':
        order_placed+=[order]
        bill+=350
    elif order.lower()=='burger':
        order_placed+=[order]
        bill+=250
    elif order.lower()=='pizza':
        order_placed+=[order]
        bill+=450
    elif order.lower()=='momos':
        order_placed+=[order]
        bill+=150
    elif order.lower()=='fries':
        order_placed+=[order]
        bill+=170
    else:
        print('We dont have this dish')
print('Your Order',order_placed)
print('Your Total Bill',bill)
print('Thank You')
Amount='''2000 , 500 , 200 , 100 , 50 , 20 , 10 , 5 , 2 , 1'''
Amount_Given=int(input(f'''\nPay Your bill.
The amount Paid should be a combination of Following notes and coins:
{Amount}.\n'''))  #In this way the user will pay the bill with the available combination of notes and coins
Amount_change=Amount_Given-bill
note2000=0
note500=0
note200=0
note100=0
note50=0
note20=0
note10=0
coin5=0
coin1=0
coin2=0
while (Amount_change>0):
    if Amount_change>=2000:
        Amount_change-=2000
        note2000+=1
    elif Amount_change>=500:
        Amount_change-=500
        note500+=1
    elif Amount_change>=200:
        Amount_change-=200
        note200+=1
    elif Amount_change>=100:
        Amount_change-=100
        note100+=1
    elif Amount_change>=50:
        Amount_change-=50
        note50+=1
    elif Amount_change>=20:
        Amount_change-=20
        note20+=1
    elif Amount_change>=10:
        Amount_change-=10
        note10+=1
    elif Amount_change>=5:
        Amount_change-=5
        coin5+=1
    elif Amount_change>=2:
        Amount_change-=5
        coin2+=1
    elif Amount_change>=1:
        Amount_change-=1
        coin1+=1
print(f''' Here\'s Your change:\n
{note2000} 2000 note
''')