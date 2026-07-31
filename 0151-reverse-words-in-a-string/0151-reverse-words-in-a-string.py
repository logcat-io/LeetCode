class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        ans = []
        target = []
        
        for ch in s:
            if ch == " ":
                if not target:
                    continue
                
                ans.append("".join(target))
                target = []
            else:
                target.append(ch)
        if target:
            ans.append("".join(target))
        
        return " ".join(ans[::-1])
