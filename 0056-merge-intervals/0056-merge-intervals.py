class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        res = []
        for i in range(len(intervals)):
            if res and intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        return res





















































        
        # intervals.sort()
        # res = []
        # for i in range(len(intervals)):
        #     if res and intervals[i][0] <= res[-1][1]:
        #         res[-1][1]= max(intervals[i][1], res[-1][1])
        #     else:
        #         res.append(intervals[i])
        # return res
               
   
        
#         res = []
#         intervals.sort()
#         for i in range(len(intervals)):
#             if res and intervals[i][0] <= res[-1][1]:
#                 res[-1][1]=max(res[-1][1], intervals[i][1])
#             else:
#                 res.append(intervals[i])
#         return res
        
        
        
#          def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         n = len(intervals)
#         intervals.sort()
#         res = []
#         for i in range(n):
#             if not res or intervals[i][0] > res[-1][1]:
#                 res.append(intervals[i])
#             else:
#                 res[-1][1] = max(res[-1][1], intervals[i][1])
#         return res
        