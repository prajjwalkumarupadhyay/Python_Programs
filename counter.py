import string 
sentence=input('Pass a statement:\n')
word=[]
for i in sentence:
    word=word+[i]
count1=0
count2=0
count3=0
count4=0
count5=0
for j in word:
    if j in string.ascii_lowercase:
        count1=count1+1
    elif j in string.ascii_uppercase:
        count2=count2+1
    elif j in string.digits:
        count3=count3+1
    elif j in string.punctuation:
        count4=count4+1
    elif j in string.whitespace:
        count5=count5+1
    
print('The sentence has: ',count1,' lowercase letters')
print('The sentence has: ',count2,' uppercase letters')
print('The sentence has: ',count3,' digits')
print('This sentence has: ',count4,' punctuations')
print('This sentence has: ',count5,' Whitespace')
