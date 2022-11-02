class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = 0
        total = sum(nums)
        for i in range(0, len(nums)):
            if i == 0:
                lsum = 0
            else:
                lsum = lsum + nums[i-1]
                
            if (total-nums[i])/2 == lsum:
                return i
            
            
        return -1
        