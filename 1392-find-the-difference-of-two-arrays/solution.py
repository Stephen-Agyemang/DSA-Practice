class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        setA = set(nums1)
        setB = set(nums2)

        list1 = []
        list2 = []
        for num in setA:
            if num not in setB:
                list1.append(num)

        for num in setB:
            if num not in setA:
                list2.append(num)


        return [list1, list2]
