class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def canShip(cap):
            ships , currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships+=1
                    currCap = cap
                currCap -= w
            return ships <= days

        l = max(weights)
        r = sum(weights)
        res = r
        while l <= r:
            cap = (l+r) // 2
            if canShip(cap):
                res = min(cap , res)
                r = cap - 1
            else:
                l = cap + 1
        return res