# from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = s.lower()
        # t = t.lower()
        # if Counter(t) == Counter(s):
        #     return True
        # return False
        
#         if len(s) != len(t):
#             return False
        
#         freq = defaultdict(int)
#         for i in range(len(s)):
#             freq[s[i]] +=1
#             freq[t[i]] -=1
            
#         for val in freq.values():
#             if val != 0:
#                 return False
#         return True
    
    
        s = s.lower()
        t = t.lower()
        return sorted(s) == sorted(t)
        
        
        