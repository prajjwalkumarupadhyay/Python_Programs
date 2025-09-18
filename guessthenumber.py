#this is guess the number game 
import random
secretnumber=random.randint(1,20)
print('i am thinking of a number between 1 to 20')
  
#ask the player to guess 6 times
for guesstaken in range(1,7):
    print('take a guess')
    guess=int(input())

    if guess>secretnumber:
        print('your guess is too high')
    elif guess<secretnumber:
        print('your guess is low')
    else:
        break #This condition is correct guess

if guess==secretnumber:
    print('Good job , you guessed my number in '+str(guesstaken)+' guesses')
else:
    print('nope the number i was thinking of was'+str(secretnumber))
    