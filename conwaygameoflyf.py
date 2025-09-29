#Conway Game of Life

import time,random,copy

width=60
height=20
# Create a list of list for the cel:

nextcells=[]
for x in range(width):
    column=[] #create a new column
    for y in range(height):
        if random.randint(0,1)==0:
            column.append('#') #Add a living cell
        else:
            column.append('') #Add a dead cell
    nextcells.append(column) #Nextcells is the list of column list

while True:
    print('\n\n\n\n\n') #Seperate each step with newlines.
    currentcells=copy.deepcopy(nextcells)
    #Print current cell on the screen
    for y in range(width):
        for x in range(height):
            print(currentcells[x][y],end='') #Print the # or space.
        print('') #Print the newline at the end of the row

    #Calculate the next few step's cell based on the current step's cells:
    for x in range(width):
        for y in range(height):
    #get neighboring coordinates:
    # % width ensures leftcoord is always b/w 0 and width -1:
            leftCoord=(x-1)%width
            rightCoord=(x+1)%width
            aboveCoord=(y-1)%height
            belowCoord=(y+1)%height 
    # Count number of living neighbors:
        numNeightbour=0
        if currentcells[leftCoord][aboveCoord] == '#':
         numNeighbors += 1 # Top-left neighbor is alive.
        if currentcells[x][aboveCoord] == '#':
         numNeighbors += 1 # Top neighbor is alive.
        if currentcells[rightCoord][aboveCoord] == '#':
         numNeighbors += 1 # Top-right neighbor is alive.
        if currentcells[leftCoord][y] == '#':
         numNeighbors += 1 # Left neighbor is alive.
        if currentcells[rightCoord][y] == '#':
         numNeighbors += 1 # Right neighbor is alive.
        if currentcells[leftCoord][belowCoord] == '#':
         numNeighbors += 1 # Bottom-left neighbor is alive.
        if currentcells[x][belowCoord] == '#':
         numNeighbors += 1 # Bottom neighbor is alive.
        if currentcells[rightCoord][belowCoord] == '#':
         numNeighbors += 1 # Bottom-right neighbor is alive.
        #Set cell based on conway's Game of Life Rules:

        if currentcells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
         # Living cells with 2 or 3 neighbors stay alive:
         nextcells[x][y] = '#'
        elif currentcells[x][y] == ' ' and numNeighbors == 3:
        # Dead cells with 3 neighbors become alive:
         nextcells[x][y] = '#'
        else:
         # Everything else dies or stays dead:
         nextcells[x][y]=''
    time.sleep(1) # Add a 1-second pause to reduce flickering.