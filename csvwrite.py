import csv
outputfile=open('example.csv','w') #For Windows , you'll have to pass newline keyword as your third argument
outputwriter=csv.writer(outputfile)
print(outputwriter.writerow(['spam','eggs','bacon','ham']))


