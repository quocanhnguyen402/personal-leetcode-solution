class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        if right - left < k:
            return arr
        while right - left >= k:
            left_value = abs(arr[left] - x)
            right_value = abs(arr[right] - x)
            if left_value > right_value:
                left += 1
            else:
                right -= 1
        return arr[left:right+1] if left != right else [arr[left]]
            