class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        best = [0] * 12
        max_score =0

        cur = [0] * 12

        def bt(idx, remain, score):
            nonlocal best, max_score

            if idx == 12:
                if score > max_score:
                    max_score = score
                    cur_copy = cur[:]
                    cur_copy[0] += remain
                    best = cur_copy
                return
            
            bt(idx+1, remain, score)

            need = aliceArrows[idx] + 1
            if need <= remain:
                cur[idx] = need
                bt(idx+1, remain - need, score + idx)
                cur[idx] = 0

        bt(0, numArrows, 0)
        return best

        