class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        
        mp = m-1
        np = n-1
        p = m+n-1
        while np >= 0:
            if mp >=0 and nums1[mp] >= nums2[np]:
                nums1[p] = nums1[mp]
                mp -=1
            else:
                nums1[p] = nums2[np]
                np -=1
            p -=1
        
        
        
        