import time
def calcprod():
    product=1
    for i in range(1,1000):
        product=product*i
    return product
startTime=time.time()
prod=calcprod()
endTime=time.time()
print(f'The result is {len(str(prod))} digits long')
print(f'Took {startTime-endTime} seconds to calculate')