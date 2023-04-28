import unittest

def circular_array_loop(nums):  

    # Write your code here
    def next_position(curr_i, next_i, d):
        res = nums[(curr_i+next_i)%len(nums)]
        d = d if d == (res<0) else None
        return (curr_i+next_i)%len(nums), res,d
    
    for i in range(len(nums)):
        # print("Num", nums[i])
        sidx, slow, sd =i, nums[i], nums[i]<0
        idx, fast, fd = i, nums[i], nums[i]<0
        count = 0
        while fd != None :
            # print("count", count)
            idx, fast, fd = next_position(idx, fast, fd)
            idx, fast, fd = next_position(idx, fast, fd)
            sidx, slow, sd = next_position(sidx, slow, sd)
            if fast == slow:
                if count<1 or idx!=i:
                    fd = None
                else:
                    return True
            
            # print("fast", idx, fast, fd)
            # print("slow", sidx, slow, sd)
            count +=1
    return False


assert circular_array_loop([1, 3, -2, -4, 1]) == True
assert circular_array_loop([2, 1, -1, -2]) == False
assert circular_array_loop([5, 4, -2, -1, 3]) == False
assert circular_array_loop([1, 2, -3, 3, 4, 7, 1]) == True
assert circular_array_loop([3, 3, 1, -1, 2]) == True