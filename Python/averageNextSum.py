# Given an array of numbers.
# Calculate how many numbers which is an average of it's preceding and succeeding numbers.
# E.g [1,2,3,7,10] should return 2 because the average of 2 and nothing is 1 and the average of 1 and 3 is 2.
# So only two of match the conditions


def find_surrounding_average(array):
    array=[0]+array+[0]
    result = 0
    for i in range(1, len(array)-1):
        if (array[i-1]+array[i+1])/2 ==array[i]:
            result+=1
    return result

array = [1, 2, 3, 7, 10, 10, 10]
print(find_surrounding_average(array))