class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        left = 0
        for i in range(len(t)):
            if left < len(s) and s[left] == t[i]:
                left += 1

        
        return left == len(s)
        