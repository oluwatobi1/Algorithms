def guess_number():
    '''Accepts users input (0-100) while guiding them to the target number'''
    import random
    num = abs(eval(input('Start Guess (number between 0-100 only): ')))
    true_num = random.randint(0,100)
    while num!=true_num or num == '': #Runs until they get the number or give up
        if num>true_num:
            print('guess is above, go lower')
            num = abs(eval(input('Retry:\n')))
        elif num<true_num:
            print('guess is below, go higher')
            num = abs(eval(input('Retry:\n')))
    print('Done', true_num)    
    return
            
guess_number()        
    