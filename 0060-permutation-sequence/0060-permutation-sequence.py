class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res, pos = [], ""
        limit = False
        used = [False] * n
        

        def bt():
            nonlocal limit, pos
            if limit: return
            if len(pos) == n:
                res.append(pos)

                if len(res) == k:
                    limit = True
                return
            
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                pos += f"{i+1}"
                bt()
                pos = pos[:-1]
                used[i] = False
        
        bt()
        return res[-1]