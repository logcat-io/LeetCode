class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_s = strs[0]

        for s in strs:
            if len(min_s) > len(s):
                min_s = s
        
        ans = ""
        stop = False
        for c in list(min_s):
            for i, v in enumerate(strs):
                if c == v[0]:
                    strs[i] = strs[i][1:]
                else:
                    stop = True
                    break
            if stop:
                break
            ans += c
        
        return ans

