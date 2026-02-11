#This Program determines the character entered by the user
char=input('Enter any key:\n')
if char.isalpha():
    print('User has entered a character ')
if char.isdigit():
    print('User has entered a digit')
if char.isspace():
    print('USer has enterd white space')