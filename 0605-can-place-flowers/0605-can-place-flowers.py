class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if n == 0:
                break
            
            if (
                flowerbed[i] == 1
                or (i > 0 and flowerbed[i-1] == 1)
                or (i < len(flowerbed) - 1 and flowerbed[i+1] == 1)
            ):
                continue

            flowerbed[i] = 1
            n -=1
        
        return n <= 0
