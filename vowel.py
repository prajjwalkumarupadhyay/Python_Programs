#Tells whether the Entered character is vowel or not
char=input('Enter a character:\n')
if (char.lower()=='a' or char.lower()=='e' or char.lower()=='i' or char.lower()=='o' or char.lower()=='u'):
    print(f'{char} is a vowel.')
else:
    print(f'{char} is not a  vowel.')
