#Restaurant bill Program

print('Welcome to our Restaurant,What would you like Order')
print('MENU')
menu={'pasta':350,'burger':250,'pizza':450,'momos':150,'french fries':170}
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
    elif order.lower()=='french fries':
        order_placed+=[order]
        bill+=170
    else:
        print('We dont have this dish')
    
print('Your Order',order_placed)
print('Your Total Bill',bill)
print('Thank You')
