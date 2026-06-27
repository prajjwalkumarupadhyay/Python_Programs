import re
def Clean_string(String):
    result=[]
    for value in String:
        value=value.strip()
        value=re.sub("[!#?]","",value)
        value=value.title()
        result.append(value)
    return result
states=[]
print("Enter names or 'Q' for exit ")
while True:
    data=input()
    if data=='Q':
        break
    states.append(data)
names=Clean_string(states)
print(names)
