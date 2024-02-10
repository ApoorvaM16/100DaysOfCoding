
class Solution:
    def mySqrt(self, x: int) -> int:
#         doing this problem using Binary Search
# we know that the squareroot lies in the range of 0 to x and it is in sorted order
# So we can use binary search
    # they said not to use this  :)
        # return int(x ** 0.5)
      
        # start, end, ans =0, x, -1
        # while start <=end:
        #     mid = start + (end - start)//2
        #     midSquare = mid * mid
        #     if midSquare > x:
        #         end = mid - 1
        #     elif midSquare < x:
        #         # ans = mid
        #         start = mid + 1
        #     else:
        #         return mid
        # return ans
        
        left, right = 0,  x
        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid

        # left > right
        return right