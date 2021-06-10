class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [ (target - p) / s for p, s in sorted(zip(position, speed))]
        res = 0
        cur = 0
        for i in range(len(time) - 1, -1, -1):
            if time[i] > cur:
                cur = time[i]
                res += 1
        return res