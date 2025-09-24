import sys,random
print('rock,paper,scissors')
#These variables keep track on number of wins,losses and ties.


win=0
lose=0
tie=0

while True:#The main game loop.
    print('%s win, %s lose,%s tie' %(win,lose,tie))
    while True:#The player input loop.
        print('Enter your move, (p)aper (s)cissors (r)ock or (q)uit')
        playermove=input()
        if playermove=='q':
            sys.exit() #Quit the program
        if playermove=='r' or playermove=='s' or playermove=='p':
            break # Break out of the input loop.

    #Display what the player chose:
    if playermove=='p':
        print('paper versus...')
    elif playermove=='s':
        print('scissors versus...')
    elif playermove=='r':
        print('rock versus.....')
    #Display what the computer chose.
    randomNumber=random.randint(1,3)
    if randomNumber==1:
        computermove='r'
        print('rock')
    elif randomNumber==2:
        computerMove='p'
        print('Paper')
    elif randomNumber==3:
        computerMove='s'
        print('scissors')
    #Display and record the win/lose/tie.
    if computerMove==playermove:
        print('Its a tie')
        tie=tie+1
    elif computerMove=='r' and  playermove=='s':
        print('You lose')
        lose=lose+1
    elif computerMove=='p' and playermove=='r':
        print('You lose')
        lose=lose+1
    elif computerMove=='s' and playermove=='p':
        print('You lose')
        lose=lose+1
    elif computerMove=='s' and playermove=='r':
        print('Its a win')
        win=win+1
    elif computerMove=='r' and playermove=='p':
        print('Its a win')
        win=win+1
    elif playermove=='s' and computerMove=='p':
        print('Its a win') 
        win=win+1
       