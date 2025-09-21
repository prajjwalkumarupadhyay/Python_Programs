#This is a Quiz Game

marks=0
print('You have 4 Questions ')

for question_number in range(1,4):
    if question_number==1:
        print('Who is the Prime Minister of India')
        answer=input()
        if answer=='Narender Modi':
            marks=marks+1
    elif question_number==2:
        print('What is the capital of India')
        answer=input()
        if answer=='New Delhi':
            marks=marks+1
    elif question_number==3:
        print('In which Year world war 1 started')
        answer=int(input())
        if answer==1914:
            marks=marks+1

print("Your final score is " + str(marks))


