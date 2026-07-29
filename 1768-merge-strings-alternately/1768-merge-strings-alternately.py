class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        answer = []
        for i in range(min_len):
            answer.append(word1[i])
            answer.append(word2[i])
        
        if len(word1) == min_len:
            answer.append(word2[min_len:])
        else:
            answer.append(word1[min_len:])
        return "".join(answer)

