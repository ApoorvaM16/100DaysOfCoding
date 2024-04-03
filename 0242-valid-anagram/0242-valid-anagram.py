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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        strMap1 = defaultdict(int)
        strMap2 = defaultdict(int)
        for i in s:
            strMap1[i] +=1
        for i in t:
            strMap2[i] +=1
        return strMap1 == strMap2
            
        
        
        