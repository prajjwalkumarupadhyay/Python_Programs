tabledata=[['Apples','Oranges','cherries','Bananas'],['Alice','Bob','Carol','David'],['Dogs','Cats','Mouse','Goose']]
for i in range(4):
    for j in range(3):
        print(tabledata[j][i],end='   ')
    print()