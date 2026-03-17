sentence=input('Type a line or paragraph.\n')
words=sentence.lower().split()
words_sorted=sorted(words)
#print(words_sorted)
ind={}
for i in range(len(words_sorted)):
    word=words_sorted[i]
    if word in ind:
        x=ind[word]
        x+=1
        ind[word]=x
    else:
        ind[word]=1
print('The following numbers indicates the repetition of that word in sentence or paragraph.')
for key,value in ind.items():
     print(key,'-',value)
