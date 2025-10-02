import pprint
message='India won the Asia Cup and beat the shit out of Pakistan by defeating them Thrice , such a humiliation but nothing new for them . They still believe that there forces shot down 6 fighter jets ,DUMBASS😂'
count={}

for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1

pprint.pprint(count)