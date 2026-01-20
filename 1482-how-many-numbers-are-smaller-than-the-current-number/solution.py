class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        hashMap = {} 
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
         
        sorted_nums = sorted(hashMap.keys())
        prefix = {}
        running_sum = 0

        for num in sorted_nums:
            prefix[num] = running_sum 
            running_sum += hashMap[num]
            print(running_sum)

        result = [] 
        for num in nums:
            result.append(prefix[num])
                
        return result    
