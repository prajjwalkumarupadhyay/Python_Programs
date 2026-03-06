import sys
def Disjointness():
    A=[]
    B=[]
    C=[]
    while True:
        a=input('Enter element in a or Type Exit to exit.\n')
        if a.upper()=='EXIT':
            break
        A.append(a)
    while True:
        b=input('Enter element in b or Type Exit to exit.\n')
        if b.upper()=='EXIT':
            break
        B.append(b)
    while True:
        c=input('Enter element in c or Type Exit to exit.\n')
        if c.upper()=='EXIT':
            break
        C.append(c)
    for a in A:
        for b in B:
            for c in C:
                if a==b==c:
                    return False
    return True
def uniquel():
    A=[]
    while True:
        a=input('Enter element in a or Type Exit to exit.\n')
        if a.upper()=='EXIT':
            break
        A.append(a)
    for j in range(len(A)):
        for k in range(j+1,len(A)):
            if A[j]==A[k]:
                return False
def sorting():
    A=[]
    while True:
        a=input('Enter element in a or Type Exit to exit.\n')
        if a.upper()=='EXIT':
            break
        A.append(a)
    temp=sorted(A)
    for j in range(1,len(temp)):
        if A[j-1]==A[j]:
            return False
    return True
def Input():
    print('''By which method you want to perform searching\n 
          1. Three-way set Disjointness.
          2. Element Uniqueness.
          3. Using Sorting\n
        Enter the respective S.NO. or Type Exit to Terminate.''')
    data=input()
    if data=="1":
        Disjointness()
    elif data=='2':
        uniquel()
    elif data=='3':
        sorting()
    elif data.upper()=='EXIT':
        sys.exit('Program Terminated.')
Input()
