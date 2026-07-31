class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u"])

        target = []
        for ch in s:
            if ch.lower() in vowels:
                target.append(ch)

        ans = []
        for ch in s:
            if ch.lower() in vowels:
                ans.append(target.pop())
            else:
                ans.append(ch)
        
        return "".join(ans)