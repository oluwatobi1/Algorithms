my_sorted_list = [1,2,3,4,100,201,202,203, 204]
my_sequences = []
for idx,item in enumerate(my_sorted_list):
  if not idx or item-1 != my_sequences[-1][-1]:
       my_sequences.append([item])
  else:
       my_sequences[-1].append(item)

print(max(my_sequences, key=len))


sorting = [1,2,3,4,100,201,202,203, 204]
sorting[-1][-1]
seq = []
for index, item in enumerate(sorting):
    print(index, item)
    if not index or item-1 != seq[-1][-1]:
        seq.append([item])
    else:
        seq[-1].append(item)
    
    
def groupSequence(lst): 
    res = [[lst[0]]] 
  
    for i in range(1, len(lst)): 
        if lst[i-1]+1 == lst[i]: 
            res[-1].append(lst[i]) 
  
        else: 
            res.append([lst[i]]) 
    return len(max(res, key=len))


        
 
 
 
 
 
        
aw = [[1,1,1,2,3], [4,100],[201,202],[203, 204]]
aw.remove([1,1,1,2,3])
rem = []
for i in aw:
    rem.extend(i)
rem