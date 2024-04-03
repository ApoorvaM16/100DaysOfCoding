class Solution:
    def removeOuterParentheses(self, s: str) -> str:
#         res,count = [],0
#         for i in range(len(s)):
#             if s[i] == '(':
#                 res.append(s[i])
#                 count +=1
#             else:
#                 res.pop()
                
#                 if res and count > 1:
#                     # count -=1
#                     res.append(s[i])
# #                 count -=1
# #         return "".join(res)
                
        
#         res, count = [], 0
#         for c in S:
#             if c == '(' and count > 0:
#                 res.append(c)
#             if c == ')' and count > 1:
#                 res.append(c)
#             if c == '(':
#                 count += 1
#             else:
#                 count-=1
#         return "".join(res)
        
        
        
        res, count = [], 0
        for c in s:
            if c == "(":
                if count > 0:
                    res.append(c)
                count +=1
            else:
                count -=1
                if count > 0:
                    res.append(c)
        return ''.join(res)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      
#         res, count = [], 0
#         for char in s:
#             if char == '(':
#                 if count > 0:
#                     res.append(char)
#                 count += 1
#             else:
#                 count -= 1
#                 if count > 0:
#                     res.append(char)
#         return ''.join(res)
