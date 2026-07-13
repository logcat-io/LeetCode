from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        left = {}

        for sc in s:
            left[sc] = left.get(sc, 0) + 1

        right = {}
        for tc in t:
            right[tc] = right.get(tc,0) +1        

        return left == right
        # return Counter(s) == Counter(t)
        

        