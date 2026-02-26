import random
randomtypo=['I will never spam my friends again.',
            'I Will Never Spam My Friends Again.',
            'i will never spam my friends again.',
            'I will Never spam my friends again.',
            'I will never Spam my friends again.',
            'I will never spam my friends Again.',
            'I will never spam My friends again.',
            'I will never spam my Friends again.']
count=0
while (count<100):
    for i in range(random.randint(0,7)):
        print(randomtypo[i])
    count+=1
