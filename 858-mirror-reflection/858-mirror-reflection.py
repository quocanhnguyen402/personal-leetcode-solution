class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        distance_travel = math.lcm(p,q)
        
        if distance_travel % (q*2) == 0:
            return 2
        else:
            if distance_travel % (2*p) == 0:
                return 0
            else:
                return 1