class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)
        return [ True if v + extraCandies >= max_c else False for i, v in enumerate(candies)]
        