name=input('Enter String\n')
char_set=set(name)
letters={'c','a','t','d','o','g'}
if letters.issubset(char_set):
    print("letters are in the name string")
else:
    print('Letters are not in the string')