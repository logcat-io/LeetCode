from collections  import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        k = len(s1)

        for i in range(0, len(s2)-k+1):
            if s1_count == Counter(s2[i:i+k]):
                return True
        
        return False
            


        