#I finally coded a recursive maleware bug that killes the kernel LOLLLL
#

def rec_coin(target, coins, outer = None):
    if not outer:
        outer = []
    for i, coin in enumerate(coins):
        out = [coin]
        j=i
        print(outer, out, j, i)
        if sum(out) == target:
            return outer.append(out)
        elif sum(out)<target and sum(out+[coins[j]])<target:
            print('recur 1', out, j, i)
            out = out + rec_coin(target, coins)
        elif sum(out)<target and sum(out+[coins[j]])>target:
            if j !=0:
                j-=1
                print('recur 2', out, j, i)
                out = out + rec_coin(target, coins)
                #reset the value of out to empty (discarding it)
            else:
                return outer.append(out)
            print(outer)
    return outer
            
            
            
        
print(rec_coin(55, [1,2,3]))