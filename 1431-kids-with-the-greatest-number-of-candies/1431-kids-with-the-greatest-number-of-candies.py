class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)
        answer = [False] * len(candies)
        for i, v in enumerate(candies):
            if v + extraCandies >= max_c:
                answer[i] = True
        
        return answer
        