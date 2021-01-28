name = 'Aaaabbbbbbbbbbbbbbccdeeeerrcgggggds'
def isDuplicate(name):
    position=1
    final_string=name[0]
    start=True
    counter=0

    while position<len(name):
        if name[position].lower()== name[position-1].lower():
            counter+=1
            if counter>2 and start:
                final_string+='['
                start=False
            final_string+=name[position]
            position+=1
        elif name[position].lower()!= name[position-1].lower():
            if not start:
                final_string+=']'
                start=True
            counter=0
            final_string+=name[position]
            position+=1       
        
    return final_string



print(isDuplicate(name))
 