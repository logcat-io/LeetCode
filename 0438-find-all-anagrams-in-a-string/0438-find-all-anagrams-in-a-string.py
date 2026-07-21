from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        cp = Counter(p)
        ans = []
        for i in range(len(s) - k + 1):
            if cp == Counter(s[i:i+k]):
                ans.append(i)
        return ans
