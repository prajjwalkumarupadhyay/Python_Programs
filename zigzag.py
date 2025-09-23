import time,sys
indent=0 #How many spaces to indent
indentincreasing=True #Whether the indentation is increasing or not.

try:
    while True: #The main program loop 
        print(''*indent,end='')
        print('********')
        time.sleep(0.1) #Pause for 1/10 of the second
        if indentincreasing:
            # Increase the number of spaces
            if indent==20:
                #Change directions:
                indentincreasing=False
            else:
                #Decrease the number of spaces:
                indent=indent-1
                if indent==0:
                    #Changes direction:
                    indentincreasing=True
except KeyboardInterrupt:
    sys.exit()