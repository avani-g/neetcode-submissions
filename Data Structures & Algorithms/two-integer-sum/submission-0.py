class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffs = {}

        for i in range(len(nums)):
            num = nums[i]
            if target - num in diffs:
                return [diffs[target - num], i]
            diffs[num] = i
        
        return [0, 0]