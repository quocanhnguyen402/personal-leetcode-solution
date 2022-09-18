class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            # Nums2 will always bigger
            return self.findMedianSortedArrays(nums2,nums1)
        else:
            len1,len2 = len(nums1),len(nums2)
            half = (len1 + len2)//2
            left = 0
            right = len1 - 1
            while True:
                mid1 = (left + right) // 2
                index2 = half-mid1-2
                left1 = nums1[mid1] if mid1 >= 0 else float("-infinity")
                right1 = nums1[mid1 + 1] if mid1 + 1 < len1 else float("infinity")
                left2 = nums2[index2] if index2 >= 0 else float("-infinity")
                right2 = nums2[index2 + 1] if index2 + 1 < len2 else float("infinity")
                
                if left1 <= right2 and left2 <= right1:
                    if (len1 + len2) % 2:
                        # odd
                        return min(right1, right2)
                    else:
                        # even
                        return (max(left1, left2) + min(right1, right2)) / 2
                if left1 > right2:
                    right = mid1 - 1
                if left2 > right1:
                    left = mid1 + 1