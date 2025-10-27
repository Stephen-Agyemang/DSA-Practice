class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        max_count = 0
        maj_element = 0
        
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            
            else:
                hashMap[num] = 1

            if hashMap[num] > max_count:
                max_count = hashMap[num]
                maj_element = num
        
        return maj_element
        
