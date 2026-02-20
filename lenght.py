print('Enter 5  random words:')
words=[]
while len(words)<5:
    word=input()
    if len(word)<6:
        print('Enter the word again')
        continue
    else:
        words.append(word)
print('5 words you entered:',words)