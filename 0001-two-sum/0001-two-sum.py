class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()
        for i in range(0, len(nums)):
            num_dict[nums[i]] = i
        for i in range(0,len(nums)):
            b = target - nums[i]
            idx = num_dict.get(b, 'NA')
            if idx!='NA' and idx!=i:
                return [i, num_dict[b]]
            
        
                        
        