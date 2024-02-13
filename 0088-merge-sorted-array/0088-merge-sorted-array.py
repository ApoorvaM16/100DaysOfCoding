class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        nums1 +=nums2
        nums1.sort()
        


        # left,right = 0,0
        # while left < m and right < n:
        #     if nums1[left] <= nums2[right]:
        #         nums1[left] = nums1[left]
        #         left +=1
        #     else:
        #         nums1[left] = nums2[right]
        #         right +=1
        # while left< m:
        #     nums1[left] = nums1[left]
        #     left +=1
        # while right < n:
        #     nums1[left] = nums2[right]
        #     right +=1
















        # nums1[:] = nums1[:m]
        # nums1[:] = nums1 + nums2
        # nums1.sort()


        # approach 2
        # n1p = m-1
        # n2p = n-1
        # pointer = m+n-1
        
        # while n2p >= 0:
        #     if n1p>=0 and nums1[n1p] > nums2[n2p]:
        #         nums1[pointer] = nums1[n1p]
        #         n1p -=1
        #     else:
        #         nums1[pointer] = nums2[n2p]
        #         n2p -=1
        #     pointer -=1
        
