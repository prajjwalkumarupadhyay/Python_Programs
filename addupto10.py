#Enter number which adds up to 10
import pyinputplus as pyip
def adduptoTen(numbers):
    numbersList=list(map(int,numbers.split(',')))
    if sum(numbersList)!=10:
        raise Exception('The digit must add up to 10')
    return numbersList
response=pyip.inputCustom(adduptoTen,prompt='Enter numbers that adds up to 10\n')
print('valid input:',response)

