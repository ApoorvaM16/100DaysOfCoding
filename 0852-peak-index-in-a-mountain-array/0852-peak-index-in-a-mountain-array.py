class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
    # O(n) TC: better approach, may not pass some testcases
        return arr.index(max(arr))      
    
    # O(logn) TC : Optimal approach


        