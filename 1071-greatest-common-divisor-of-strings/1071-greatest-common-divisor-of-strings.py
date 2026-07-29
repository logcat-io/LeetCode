class Solution:

    def divides(self, base, s):
        if len(s) % len(base) != 0:
            return False
        return base * (len(s) // len(base)) == s
        
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        
        for L in range(len(str2), 0, -1):
            base = str2[:L]
            if self.divides(base, str1) and self.divides(base, str2):
                return base
        return ""