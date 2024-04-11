class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        count,res = 0, ""
        for i in s:
            if i == '(':
                if count >0:
                    res +=i
                count +=1
            else:
                count -= 1
                if count > 0:
                    res +=i
        return res
                    
        
        
        
    
        
        
        
#         res, count = [], 0
#         for c in s:
#             if c == "(":
#                 if count > 0:
#                     res.append(c)
#                 count +=1
#             else:
#                 count -=1
#                 if count > 0:
#                     res.append(c)
#         return ''.join(res)
        
        

