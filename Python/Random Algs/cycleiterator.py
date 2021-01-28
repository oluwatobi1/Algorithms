arr = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday"]

def cycleiterator(arr):

    """
    This demonstrates closure
    """
    counter=0
    def iterateitems():
        nonlocal counter       
        counter+=1
        print(arr[counter%len(arr)])
    
    return iterateitems

func = cycleiterator(arr)
func()
func()
func()


