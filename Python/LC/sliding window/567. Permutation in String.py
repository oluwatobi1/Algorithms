# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.
# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen, temp = {}, {}
        for char in s1:
            seen[char]= seen.get(char, 0)+1
            temp[char]=temp.get(char, 0)+1           
            
        window_start = 0
        window_end = 0
        while window_end<len(s2):
            curr_char = s2[window_end]
            if seen.get(curr_char, False):
                if temp.get(curr_char, False):
                    temp[curr_char]-=1
                    if temp[curr_char]==0:
                        del temp[curr_char]
                else:
                    temp[curr_char]=temp.get(curr_char, 0)-1    
                    
            if window_end>len(s1)-1:
                leaving_char = s2[window_start]
                if seen.get(leaving_char, False):
                    if temp.get(leaving_char, False):
                        temp[leaving_char]+=1                        
                        if temp[leaving_char]==0:
                            del temp[leaving_char]
                    else:
                        temp[leaving_char]=temp.get(leaving_char, 0)+1
                        
                window_start+=1
            if len(temp)<1:
                return True
            window_end+=1           
            
        return False
                