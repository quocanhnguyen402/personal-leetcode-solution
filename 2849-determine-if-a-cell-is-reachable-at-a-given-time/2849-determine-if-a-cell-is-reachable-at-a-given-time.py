class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        width = abs(sx-fx)
        height = abs(sy-fy)
        if width == height == 0 and t == 1:
            return False
        max_step = width + height
        step_can_skip = min(width,height)
        min_step = max_step - step_can_skip
        return min_step <= t
        