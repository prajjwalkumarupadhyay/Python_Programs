def bus():
  time=int(input('for how many hours your vehicle was parked.\n'))
  bill=20*time
  return bill
def car():
  time=int(input('for how many hours your vehicle was parked.\n'))
  bill=10*time
  return bill
def motorcycle():
  time=int(input('for how many hours your vehicle was parked.\n'))
  bill=5*time
  return bill
def choose_Vehicle():
  print('''\n\tChoose your vehicle Type.\n
      1. Type B for bus
      2. Type C for car
      3. Type M for motorcycle/cycle/scooter.''') 
  val=input()
  try:
    if val.upper()=='B':
     pay=bus()
     print('Your total bill is: ',pay)
    elif val.upper()=='C':
     pay=car()
     print('Your total bill is: ',pay) 
    elif val.upper()=='M':
     pay=motorcycle()
     print('Your total bill is: ',pay) 
    else:
      raise ValueError('Invalid Value.')
  except ValueError as e:
   print(e)
   choose_Vehicle()

choose_Vehicle()

