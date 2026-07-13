from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mc = Counter(magazine)
        rc = Counter(ransomNote)
        
        for r in rc:
            if mc[r] < rc[r]:
                return False 
        
        return True
        