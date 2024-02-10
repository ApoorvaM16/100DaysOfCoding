class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
    # O(n) TC: better approach, may not pass some testcases
        # return arr.index(max(arr))      
    
    # O(logn) TC : Optimal approach

        start, end = 0, len(arr) - 1
        while start < end :
            mid = start + (end - start)//2
            if arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid
            
        return start
        