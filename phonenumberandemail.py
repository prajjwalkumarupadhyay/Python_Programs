#Find phone number and email address
import re
#Create Phone number regex
phoneregex=re.compile(r'(\+\d{12})')
#Create email address regex
emailregex=re.compile(r'''
                     [A-Za-z0-9._%+-]+
                      @
                      [A-Za-z]+
                      \.[A-Za-z]{2,} ''',re.VERBOSE)
#Find the matches 
text='My phone number is +913376892180 and my email id is abcdefg@gamil.com'
matches=[]
for i in phoneregex.findall(text):
    matches+=[i]
for i in emailregex.findall(text):
    matches+=[i]

print(matches)