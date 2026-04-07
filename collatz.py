#This is collatz Program
import sys
def main():
    def collatz(number):
        if number%2==0:
            print(number//2)
            return number//2
        else:
            print(3*number+1)
            return 3*number+1
    try:
        user=int(input('Enter an integer.\n'))
    except ValueError:
        print('Error:Enter Correct Value:')
        main()
    value=collatz(user)
    while value>1:
        value=collatz(value)
    else:
        sys.exit()
main() 