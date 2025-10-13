# This program checks if the input is a phone number or not 

def isphonenumber(text):
    if len(text)!=12:
        return False
    for i in range(1,3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?')
print(isphonenumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isphonenumber('Moshi moshi'))