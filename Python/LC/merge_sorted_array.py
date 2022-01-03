def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for curr in range(0, n):
            for i in range(0, m+n):
                if (nums1[i]<nums2[curr]) and i<m+curr:
                    continue
                else:
                    nums1.insert(i, nums2[curr])
                    nums1.pop() 
                    break                                 
        return nums1