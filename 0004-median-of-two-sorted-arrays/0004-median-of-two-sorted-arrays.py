class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = sorted(nums1 + nums2)
        mid = nums1[len(nums1) // 2]
        if len(nums1) % 2 == 0:
            sMid = nums1[(len(nums1) // 2) - 1]
            return (mid + sMid) / 2
        return mid