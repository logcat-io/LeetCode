from collections import defaultdict, Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 총 길이 - 제일 많이 나온거 <= k 이면 변경이 가능하다.
        if len(s) == 1:
            return 1

        count = Counter()
        left = 0
        max_count = 0
        best = 0

        for right, ch in enumerate(s):
            count[ch] += 1
            max_count = max(max_count, count[ch])

            while (right - left  + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            
            best = max(best, right - left + 1)
            
        return best  
