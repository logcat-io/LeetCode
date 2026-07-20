import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        regx = r"[^a-zA-Z0-9]"
        clean = re.sub(regx, '', s).lower()

        lo, hi = 0, len(s) - 1
        while lo < hi:
            if not s[lo].isalnum():
                lo += 1
                continue
            elif not s[hi].isalnum():
                hi -=1
                continue

            if s[lo].lower() != s[hi].lower():
                return False
            lo += 1
            hi -= 1
        
        return True
        
        