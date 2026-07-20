import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        regx = r"[^a-zA-Z0-9]"
        clean = re.sub(regx, '', s).lower()
        return clean == clean[::-1]
        
        