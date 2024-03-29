from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        t = t.lower()
        if Counter(t) == Counter(s):
            return True
        return False
        
        
        