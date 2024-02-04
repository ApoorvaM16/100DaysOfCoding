class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    # Using extra space  O(n) TC and O(n) SC
        # dic = {}
        # for i in nums:
        #     if i in dic:
        #         dic[i] +=1
        #     else:
        #         dic[i] = 1
        # for key, val in dic.items():
        #     if val ==1:
        #         return key

# O(n) TC O(1) SC
        xor = 0
        for i in nums:
            xor ^=i
        return xor


        