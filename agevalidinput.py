while True:
    age=input('Enter your age:\n')
    try:
        age=int(age)
    except:
        print('The age should be in numeric digits')
        continue
    if age<1:
        print('Please enter positive number')
        continue
    break
print(f'Your age is {age}')
