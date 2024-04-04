class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        maxLen, maxStr = 1, s[0]
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            for j in range(i):
                if s[i] == s[j] and (i-j<=2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > maxLen:
                        maxLen = i-j+1
                        maxStr = s[j:i+1]
        return maxStr
        
