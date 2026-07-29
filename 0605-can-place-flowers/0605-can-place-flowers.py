class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        if len(flowerbed) == 1:
            if n == 0:
                return True
            else:
                if flowerbed[0] == 1:
                    return False
                else:
                    return True
        
        for i in range(len(flowerbed)):
            if n == 0: break
            if i == 0:
                if flowerbed[1] == 0 and flowerbed[0] == 0:
                    flowerbed[0] = 1
                    n-=1
                continue
            
            if i == len(flowerbed) - 1:
                if flowerbed[-2] == 0 and flowerbed[-1] == 0:
                    flowerbed[-1] = 1
                    n -= 1
                continue
            
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                
        
        return n == 0
