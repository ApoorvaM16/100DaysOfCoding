from math import floor
class Solution:
    def mySqrt(self, x: int) -> int:
#         doing this problem using Binary Search
# we know that the squareroot lies in the range of 0 to x and it is in sorted order
# So we can use binary search


        # if x == 0:
        #     return 0
        # elif x == 1: return 1
        start, end,ans =0, x, -1
        while start <=end:
            mid = start + (end - start)//2
            midSquare = mid * mid
            if midSquare > x:
                end = mid - 1
            elif midSquare < x:
                ans = mid
                start = mid + 1
            else:
                return mid
        return ans
        