  
def bin(ls_int, lower_limits, out = None, cnt = None):
    if out == None:
        out = []
        cnt = 1
    if ls_int[-1] <= lower_limits[0]:
        print('end', ls_int, lower_limits)
        
        out.append(cnt)
        return out[::-1]   
    elif ls_int[-1] > lower_limits[-1]:
        print('count recurs', cnt, ls_int, lower_limits)
        cnt+=1
        bin(ls_int[:-1], lower_limits, out, cnt)
        
    elif ls_int[-1]<= lower_limits[-1]:
        print('recurs only', ls_int, lower_limits)
        out.append(cnt)
        cnt = 1
        bin(ls_int[:-1], lower_limits[:-1], out, cnt)
        
    return out[::-1]

print(bin([-2,1,2,3,5,6,7,8,9,10,11,12],[-2,5,10]))