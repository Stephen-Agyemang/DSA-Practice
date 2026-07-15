class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results = set()
        set1 = set(nums1)

        for num in nums2: 
            if num in set1:
                results.add(num)

        return list(results)
