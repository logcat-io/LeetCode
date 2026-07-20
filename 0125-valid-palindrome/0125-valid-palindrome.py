import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        regx = r"[^a-zA-Z0-9]"
        clean = re.sub(regx, '', s).lower()

        lo, hi = 0, len(clean) - 1
        while lo < hi:
            if clean[lo] != clean[hi]:
                return False
            lo += 1
            hi -= 1
        
        return True
        
        